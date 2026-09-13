import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY_SCRIPT = ROOT / "scripts" / "verify_repository_policy.py"


def _load_policy_module():
    spec = importlib.util.spec_from_file_location("verify_repository_policy", POLICY_SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_repository_policy_passes():
    module = _load_policy_module()
    assert module.main() == 0


def test_unicode_dash_policy_covers_en_and_em_dash():
    module = _load_policy_module()
    assert "\u2013" in module.PROHIBITED_DASHES
    assert "\u2014" in module.PROHIBITED_DASHES
