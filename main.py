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
from lxdbackup.backup_commands import ArgBuilder, SyncoidArgs

from config.base_config import BaseConfig

FILENAME = ".config.yml"
PREFIX = "https://"


def main():
    # lxd_client = Client()
    # config = get_base_config()
    # api = get_api(config)
    # lxd = Lxd(config=config, api=api)
    # lxd.list_containers()
    ###

    z_src = ZfsUtil(host="p21")
    z_src.set_source_container("mattermost")

    z_dst = ZfsUtil(host="p21")
    z_dst.set_destination_container("mattermost-copy")

    args = SyncoidArgs(
        zfs_source_path=z_src.source_container_path,
        zfs_destination_path=z_dst.destination_container_path,
    )
    built_args = ArgBuilder(args=args)
    print(built_args)

    # todo pseudo code below
    l = LxdBackup(src_host="p21", dst_host="p21")
    l.set_backup_src(
        path=LxdBackupSource(
            backup_source_host="p21",
            selected_backup_source_dataset=z_src.get_path("mattermost"),
        ),
    )
    l.set_backup_dst(
        path=LxdBackupDestination(
            backup_destination_host="p20",
            selected_backup_destination_dataset=z_dst.set_path("mattermost"),
        )
    )
    l.run_backup(cmd=built_args)


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
