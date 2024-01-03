import pytest

pytestmark = [
    pytest.mark.requires_salt_states("grafana.exampled"),
]


@pytest.fixture
def grafana(states):
    return states.grafana


def test_replace_this_this_with_something_meaningful(grafana):
    echo_str = "Echoed!"
    ret = grafana.exampled(echo_str)
    assert ret.result
    assert not ret.changes
    assert echo_str in ret.comment
