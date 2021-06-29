import yaml
import os
from enum import Enum, auto
from dataclasses import dataclass
import pytest

import confuse

# from pytest import fixture
from pytest_cases import fixture


def test_get_endpoint_url(self):
    prefix = "https://"
    host = self.config["lxd"]["api"][0]["endpoint"].get()
    return f"{prefix}{host}"
    
def test_get_auth(self, auth_type):
    return str(self.config["lxd"]["api"][0]["auth"][auth_type])
