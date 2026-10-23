import json
from pathlib import Path


CONTRACT = Path(__file__).resolve().parents[2] / "contracts" / "cycle_clear.py"
PROMPT = "Determine whether each directed barter offer satisfies"


def edge(giver, receiver, status):
    return {"giver": giver, "receiver": receiver, "status": status}


def three_cycle_edges(accounts):
    alice, bob, carol = accounts
    return [
        edge(alice, bob, "FITS"), edge(alice, carol, "DOES_NOT_FIT"),
        edge(bob, alice, "DOES_NOT_FIT"), edge(bob, carol, "FITS"),
        edge(carol, alice, "FITS"), edge(carol, bob, "DOES_NOT_FIT"),
    ]


def response(edges):
    return json.dumps({"edges": edges})


def prepare(vm, contract, accounts, senders):
    vm.sender = senders[0]
    contract.open_round("spring_swap", "Neighbors exchanging useful surplus household goods.")
    vm.sender = senders[0]
    contract.register_intent("spring_swap", "A working hand drill.", "A step ladder.")
    vm.sender = senders[1]
    contract.register_intent("spring_swap", "A step ladder.", "A drill bit set.")
    vm.sender = senders[2]
    contract.register_intent("spring_swap", "A drill bit set.", "A working hand drill.")
    vm.sender = senders[0]
    contract.freeze_round("spring_swap")


def deploy_round(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie):
    contract = direct_deploy(str(CONTRACT), sdk_version="v0.2.16")
    accounts = ["0x" + direct_alice.hex(), "0x" + direct_bob.hex(), "0x" + direct_charlie.hex()]
    senders = [direct_alice, direct_bob, direct_charlie]
    prepare(direct_vm, contract, accounts, senders)
    return contract, accounts, senders


def test_three_party_cycle_requires_every_selected_member_to_accept(
    direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie
):
    contract, accounts, senders = deploy_round(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie)
    direct_vm.mock_llm(PROMPT, response(three_cycle_edges(accounts)))
    contract.assess_round("spring_swap")
    assert contract.get_round("spring_swap")["selected_cycle"] == accounts
    for sender in senders[:-1]:
        direct_vm.sender = sender
        contract.accept_cycle("spring_swap")
        assert contract.get_round("spring_swap")["status"] == "AWAITING_ACCEPTANCE"
    direct_vm.sender = senders[-1]
    contract.accept_cycle("spring_swap")
    assert contract.get_round("spring_swap")["status"] == "CLEARED"
    leader = direct_vm._captured_validators[-1][0]
    assert direct_vm.run_validator(leader_result=leader) is True


def test_cycle_is_found_without_a_direct_two_party_swap(
    direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie
):
    contract, accounts, _ = deploy_round(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie)
    edges = three_cycle_edges(accounts)
    assert not (edges[0]["status"] == "FITS" and edges[2]["status"] == "FITS")
    direct_vm.mock_llm(PROMPT, response(edges))
    contract.assess_round("spring_swap")
    assert contract.get_round("spring_swap")["selected_cycle"] == accounts


def test_forged_or_incomplete_edge_list_fails_closed(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie):
    contract, _, _ = deploy_round(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie)
    direct_vm.mock_llm(PROMPT, response(three_cycle_edges(["a", "b", "c"])[:-1]))
    with direct_vm.expect_revert("wrong_edge_count"):
        contract.assess_round("spring_swap")
    assert contract.get_round("spring_swap")["status"] == "FROZEN"
    assert contract.get_round("spring_swap")["judgments"] == []


def test_creator_and_nonmember_guards(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie):
    contract, accounts, _ = deploy_round(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie)
    direct_vm.sender = direct_bob
    with direct_vm.expect_revert("only_round_creator"):
        contract.freeze_round("spring_swap")
    direct_vm.sender = direct_alice
    direct_vm.mock_llm(PROMPT, response(three_cycle_edges(accounts)))
    contract.assess_round("spring_swap")
    direct_vm.sender = bytes.fromhex("44" * 20)
    with direct_vm.expect_revert("caller_not_in_selected_cycle"):
        contract.accept_cycle("spring_swap")

