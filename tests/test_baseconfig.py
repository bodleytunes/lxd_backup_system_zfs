import yaml
import os
from enum import Enum, auto
from dataclasses import dataclass
import pytest

import confuse

# from pytest import fixture
from pytest_cases import fixture


@pytest.fixture(autouse=True)
def config() -> confuse.Configuration:
    config = confuse.Configuration("lxdbackup", __name__)
    config.set_file(".config.yml")
    return config


def test_set_endpoint_host(config):
    host = config["lxd"]["api"][0]["endpoint"].get()
    assert host == "10.55.0.21:8443"

    """def get_endpoint_url(self):
        return f"{self.prefix}{self.host}"

    def get_auth(self, auth_type):
        return str(self.config["lxd"]["api"][0]["auth"][auth_type])
"""
