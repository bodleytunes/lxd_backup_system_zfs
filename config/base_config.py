import yaml
import os
from enum import Enum, auto
from dataclasses import dataclass
import pytest

import confuse

# from pytest import fixture
from pytest_cases import fixture


class BaseConfig:
    def __init__(self, config) -> None:
        self.config = config
        pass

    def get_endpoint_url(self):
        prefix = "https://"
        host = self.config["lxd"]["api"][0]["endpoint"].get()
        return f"{prefix}{host}"

    def get_auth(self, auth_type):
        return str(self.config["lxd"]["api"][0]["auth"][auth_type])
