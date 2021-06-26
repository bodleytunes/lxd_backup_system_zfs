import yaml
import os
from enum import Enum, auto
from dataclasses import dataclass
import pytest

import confuse

# from pytest import fixture
from pytest_cases import fixture

config_file = dict(
    {
        "lxd": {"api": {"auth": {"cert": "./client.crt", "key": "./client.key"}}},
        "credentials": {
            "username": "root",
            "password": "egNim3dRR9qATkxKaUA3",
            "hostname": "10.55.0.66",
        },
    }
)


@dataclass
class ConfigItem:
    item: str
    config_file: str


class BaseConfig:

    config: dict

    def __init__(self, filename) -> None:

        self.filename = filename
        pass

    def get_config_item(self, item):

        config = self._get_file(self.filename)
        item = self._find_item(item, config)
        return item

    def _find_item(self, item, config):

        for _, value in config.items():
            if item in value:
                return value[item]

    @staticmethod
    def get_username(filename):

        if os.getenv("USERNAME") is not None:
            username = os.environ.get("USERNAME")
        else:
            creds = BaseConfig._get_file(filename)
            username = creds["credentials"]["username"]

        return username

    @staticmethod
    def get_password(filename):

        if os.getenv("PASSWORD") is not None:
            PASSWORD = os.environ.get("PASSWORD")
        else:
            creds = BaseConfig._get_file(filename)

            PASSWORD = creds["credentials"]["password"]

        return PASSWORD

    @staticmethod
    def get_hostname(filename):

        if os.getenv("HOSTNAME") is not None:
            HOSTNAME = os.environ.get("HOSTNAME")
        else:
            creds = BaseConfig._get_file(filename)

            HOSTNAME = creds["credentials"]["hostname"]

        return HOSTNAME

    @staticmethod
    def get_cert(filename):

        if os.getenv("CERT") is not None:
            certs = os.environ.get("CERT")
        else:
            creds = BaseConfig._get_file(filename)

            HOSTNAME = creds["lxd"]["api"]["certs"]

        return HOSTNAME

    def _get_file(self, filename):

        with open(filename) as file:
            item = yaml.load(file, Loader=yaml.FullLoader)
            return item
