import pytest

pytestmark = [
    pytest.mark.requires_salt_modules("grafana.example_function"),
]


@pytest.fixture
def grafana(modules):
    return modules.grafana


def test_replace_this_this_with_something_meaningful(grafana):
    echo_str = "Echoed!"
    res = grafana.example_function(echo_str)
    assert res == echo_str
