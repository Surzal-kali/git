import pytest

from smoke_check import (
    check_mgscripts_load_env,
    check_documents_build_namespace,
    check_computerspeak,
    check_packet_sniffer_importable,
    check_target_config,
)


@pytest.mark.parametrize("check_fn", [
    check_mgscripts_load_env,
    check_documents_build_namespace,
    check_computerspeak,
    check_packet_sniffer_importable,
    check_target_config,
])
def test_smoke_checks(check_fn):
    """Run each smoke-check helper and assert it returns success."""
    ok, msg = check_fn()
    assert ok, msg
