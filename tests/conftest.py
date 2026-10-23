from pathlib import Path

from tests.windows_compat import install

install()


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "cycle_clear.py"
SDK_VERSION = "v0.2.16"


def deploy(direct_deploy, sender):
    return direct_deploy(str(CONTRACT), sdk_version=SDK_VERSION)
