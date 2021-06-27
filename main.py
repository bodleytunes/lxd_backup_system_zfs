from typing import List
from pylxd import Client as Api


from lxdbackup.backup import (
    BackupLxdCommand,
    ListNetworksLxdCommand,
    ListLxdCommand,
    Orchestrator,
    Lxd,
    Server,
    BackupParams,
    BackupArchive,
)

from pydantic.main import BaseConfig
import confuse
from lxdbackup import backup, connection
from config.base_config import BaseConfig, ConfigItem

FILENAME = ".config.yml"


def main():
    # lxd_client = Client()
    config = get_base_config()
    get_api(config)


def get_base_config():
    # use confuse to parse config file
    config = confuse.Configuration("lxdbackup", __name__)
    config.set_file(".config.yml")
    return config


def get_api(config):
    api = Api(
        endpoint=create_endpoint_url(config),
        verify=False,
        cert=create_auth(config, "cert"),
    )
    return api


def create_endpoint_url(config):
    prefix = "https://"
    host = config["lxd"]["api"][0]["endpoint"].get()
    return f"{prefix}{host}"


def create_auth(config, auth_type):
    return str(config["lxd"]["api"][0]["auth"][auth_type])


if __name__ == "__main__":
    main()
