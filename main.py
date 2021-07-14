from typing import List
from pylxd import Client as Api
from pydantic.main import BaseConfig
import confuse


from lxdbackup.lxd import (
    LxdBackup,
    LxdBackupSource,
    LxdBackupDestination,
)
from lxdbackup.zfs import ZfsUtil
from lxdbackup.backup_commands import ArgBuilder, SyncoidArgs, CommandRunner

from config.base_config import BaseConfig

FILENAME = ".config.yml"
PREFIX = "https://"


def main():

    z_src = ZfsUtil(host="p21")
    z_src.set_source_container("mattermost")

    z_dst = ZfsUtil(host="p21")
    z_dst.set_destination_container("mattermost-copy")

    args = SyncoidArgs(
        zfs_source_path=z_src.source_container_path,
        zfs_destination_path=z_dst.destination_container_path,
    )
    cmd = ArgBuilder(args=args)
    print(cmd.arg_string)
    # now subprocess.run the above string.

    # todo pseudo code below
    run = CommandRunner(cmd.arg_string)
    run.backup()


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
