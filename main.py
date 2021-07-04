from typing import List
from pylxd import Client as Api
from pydantic.main import BaseConfig
import confuse


from lxdbackup.lxd import (
    BackupLxdCommand,
    ListNetworksLxdCommand,
    ListLxdCommand,
    Orchestrator,
    Lxd,
    Server,
    BackupParams,
    BackupArchive,
)
from config.util import SyncoidArgs, ArgBuilder, ZfsUtil

from config.base_config import BaseConfig
from lxdbackup.lxd import Lxd

FILENAME = ".config.yml"
PREFIX = "https://"


def main():
    # lxd_client = Client()
    # config = get_base_config()
    # api = get_api(config)
    # lxd = Lxd(config=config, api=api)
    # lxd.list_containers()
    ###
    """
    args = SyncoidArgs()
    built_args = ArgBuilder(args=args)
    print(built_args)
    """
    z = ZfsUtil(host="p21")
    z.get_pool_names()
    z.get_pool_datasets()


def get_base_config() -> confuse.Configuration:
    # use confuse to parse config file
    config = confuse.Configuration("lxdbackup", __name__)
    config.set_file(FILENAME)
    return config


def get_api(config) -> Api:
    base_cfg = BaseConfig(config, PREFIX)
    try:
        api = Api(
            endpoint=base_cfg.get_endpoint_url(),
            verify=False,
            cert=base_cfg.get_auth("cert"),
        )
    except Exception as e:
        raise ConnectionAbortedError(f"computer says no {e}")

    return api


if __name__ == "__main__":
    main()
