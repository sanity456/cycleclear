import copy
import json
from tests.direct.test_cycle_clear import CONTRACT, PROMPT, deploy_round, response, three_cycle_edges, round_key


def test_creator_capacity_and_names_are_isolated(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie):
    contract = direct_deploy(str(CONTRACT), sdk_version="v0.2.16")
    members = ["0x" + account.hex() for account in (direct_alice, direct_bob, direct_charlie)]
    direct_vm.sender = direct_alice
    for index in range(20):
        contract.open_round(f"round_{index}", "Household barter.", members)
    with direct_vm.expect_revert("creator_round_limit_reached"):
        contract.open_round("overflow", "Household barter.", members)
    direct_vm.sender = direct_bob
    own = contract.open_round("round_0", "Independent owner's round.", members)
    assert contract.get_round(own)["creator"] == members[1]
    original = members[0] + "|round_0"
    assert contract.get_round(original)["context"] == "Household barter."
    with direct_vm.expect_revert("invalid_round_id"):
        contract.open_round(original, "Cannot impersonate another creator.", members)
    with direct_vm.expect_revert("only_round_creator"):
        contract.freeze_round(original)


def test_uninvited_enrollment_cannot_consume_slots(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie):
    contract = direct_deploy(str(CONTRACT), sdk_version="v0.2.16")
    members = ["0x" + account.hex() for account in (direct_alice, direct_bob, direct_charlie)]
    direct_vm.sender = direct_alice
    reference = contract.open_round("private_roster", "Household barter.", members)
    direct_vm.sender = bytes.fromhex("44" * 20)
    before = contract.get_round(reference)
    with direct_vm.expect_revert("caller_not_invited"):
        contract.register_intent(reference, "Unsolicited offer.", "Unsolicited need.")
    assert contract.get_round(reference) == before


def test_validator_rejects_forged_edge_even_if_cycle_is_unchanged(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie):
    contract, accounts, _ = deploy_round(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie)
    direct_vm.mock_llm(PROMPT, response(three_cycle_edges(accounts)))
    contract.assess_round(round_key(direct_alice))
    leader = copy.deepcopy(direct_vm._captured_validators[-1][0])
    leader["edges"][1]["status"] = "UNCERTAIN"
    assert direct_vm.run_validator(leader_result=leader) is False


def test_terminal_cycle_rejects_replay_and_decline(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie):
    contract, accounts, senders = deploy_round(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie)
    key = round_key(direct_alice)
    direct_vm.mock_llm(PROMPT, response(three_cycle_edges(accounts)))
    contract.assess_round(key)
    for sender in senders:
        direct_vm.sender = sender
        contract.accept_cycle(key)
    before = contract.get_round(key)
    for method in (contract.accept_cycle, contract.decline_cycle):
        with direct_vm.expect_revert("cycle_not_awaiting_acceptance"):
            method(key)
    with direct_vm.expect_revert("round_not_frozen"):
        contract.assess_round(key)
    assert contract.get_round(key) == before
