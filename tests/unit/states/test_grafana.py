import pytest
import salt.modules.test as testmod
import saltext.grafana.modules.grafana_mod as grafana_module
import saltext.grafana.states.grafana_mod as grafana_state


@pytest.fixture
def configure_loader_modules():
    return {
        grafana_module: {
            "__salt__": {
                "test.echo": testmod.echo,
            },
        },
        grafana_state: {
            "__salt__": {
                "grafana.example_function": grafana_module.example_function,
            },
        },
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    expected = {
        "name": echo_str,
        "changes": {},
        "result": True,
        "comment": f"The 'grafana.example_function' returned: '{echo_str}'",
    }
    assert grafana_state.exampled(echo_str) == expected
