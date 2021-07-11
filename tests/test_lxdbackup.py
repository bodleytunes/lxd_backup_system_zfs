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

CONTAINER = "mattermost"


@pytest.fixture(autouse=True)
def api(config):
    cert = ("tests/test_client.crt", "tests/test_client.key")
    try:
        api = Api(
            endpoint="https://10.55.0.21:8443",
            verify=False,
            cert=cert,
        )
    except Exception as e:
        raise ConnectionAbortedError(f"computer says no {e}")

    return api


@pytest.fixture(autouse=True)
def container():
    return CONTAINER


@pytest.mark.tests
def test_api_ok(api):
    assert isinstance(api, Api)


@pytest.mark.tests
def test_list_containers(api):
    containers = api.containers.all()
    assert isinstance(containers, list)


@pytest.mark.tests
def test_get_container(api, container):
    instance = api.instances.get(container)
    assert instance.name == container
