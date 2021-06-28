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
from config.base_config import BaseConfig

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
    cfg = BaseConfig(config)
    api = Api(
        endpoint=cfg.get_endpoint_url(),
        verify=False,
        cert=cfg.get_auth("cert"),
    )
    return api


if __name__ == "__main__":
    main()
