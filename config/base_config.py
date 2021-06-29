from confuse.core import Configuration
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
        self.config: confuse.Configuration = config
        self.prefix: str = "https://"
        self._set_endpoint_host()
        pass

    def _set_endpoint_host(self):
        self.host: str = self.config["lxd"]["api"][0]["endpoint"].get()

    def get_endpoint_url(self):
        return f"{self.prefix}{self.host}"

    def get_auth(self, auth_type):
        return str(self.config["lxd"]["api"][0]["auth"][auth_type])
