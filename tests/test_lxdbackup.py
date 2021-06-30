import yaml
import os
from enum import Enum, auto
from dataclasses import dataclass
import pytest
from pytest_cases import fixture
from pylxd import Client as Api
import confuse


from config.base_config import BaseConfig
from tests.test_baseconfig import config, prefix_https


@pytest.fixture(autouse=True)
def api(config):
    try:
        api = Api(
            endpoint="https://10.55.0.21:8443",
            verify=False,
            cert="tests/test_client.crt",
        )
    except Exception as e:
        raise ConnectionAbortedError(f"computer says no {e}")

    return api


def test_list_containers(api):
    assert api
