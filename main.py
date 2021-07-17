from typing import List
from enum import Enum, auto
import asyncio
from pylxd import Client as Api
from pydantic.main import BaseConfig
from dataclasses import dataclass
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


@dataclass
class CopyParams:
    src_host: str
    src_host_user: str
    dst_host: str
    dst_host_user: str


def main():
    copy_params = build_copy_params()

    z_src = setup_source(copy_params)
    z_dst = setup_dest(copy_params)

    args = build_args(z_src, z_dst)
    cmd = ArgBuilder(args=args)
    run = CommandRunner(cmd.arg_string)
    do_backup(run)


def build_copy_params():
    copy_params = CopyParams(
        src_host="p21", src_host_user="root", dst_host="p21", dst_host_user="root"
    )
    return copy_params
    # run backup
    # todo: if host is not local running host, then ssh via paramiko and then run commands locally
    # todo: change backup.yaml file in mounted lxd to suit new storage pools and location
    # todo: lxd unmount
    # todo: lxd import
    # todo: live monitor of process output, threading, asyncio etc
    # todo: run all including syncoid in a bundled docker container or just run from docker container on the source
    # host by default
    # run.backup()
    # print(run.result)
    # logging(run)
    # asyncio


def do_backup(run):
    # loop = asyncio.get_event_loop()
    result = asyncio.run(run.backup())
    # print(result)
    # loop.close()


def logging(run):
    log = Log()
    log.log(run.result["stdout"], run.result["stderr"])


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


def setup_dest(copy_params):
    z_dst = ZfsUtil(host=copy_params.src_host, user=copy_params.src_host_user)
    z_dst.set_destination_container(copy_params.dst_host_container)
    return z_dst


def setup_source(copy_params):
    z_src = ZfsUtil(host=copy_params.dst_host, user=copy_params.dst_host_user)
    z_src.set_source_container(copy_params.dst_host_container)
    return z_src


if __name__ == "__main__":
    main()
