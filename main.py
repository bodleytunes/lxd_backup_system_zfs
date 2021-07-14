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
from lxdbackup.backup_logs import Log

from config.base_config import BaseConfig

FILENAME = ".config.yml"
PREFIX = "https://"


def main():

    z_src = setup_source()
    z_dst = setup_dest()

    args = build_args(z_src, z_dst)
    cmd = ArgBuilder(args=args)
    run = CommandRunner(cmd.arg_string)
    # run backup
    # todo if host is not local running host, then ssh
    # todo: change backup.yaml in lxd to suit new storage
    # todo: lxd mount
    # todo: lxd import
    run.backup()
    print(run.result)
    logging(run)


def logging(run):
    log = Log()
    log(run.result["stdout"], run.result["stderr"])


def build_args(z_src, z_dst):
    args = SyncoidArgs(
        src_host=z_src.host,
        src_user=z_src.user,
        dst_host=z_dst.host,
        dst_user=z_dst.user,
        zfs_source_path=z_src.source_container_path,
        zfs_destination_path=z_dst.destination_container_path,
    )

    return args


def setup_dest():
    z_dst = ZfsUtil(host="p21", user="root")
    z_dst.set_destination_container("mattermost-copy")
    return z_dst


def setup_source():
    z_src = ZfsUtil(host="p21", user="root")
    z_src.set_source_container("mattermost")
    return z_src


if __name__ == "__main__":
    main()
