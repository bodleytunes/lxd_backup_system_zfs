from typing import List
from enum import Enum, auto
import asyncio
from pydantic.main import BaseConfig
from dataclasses import dataclass
import confuse


from lxdbackup.lxd import (
    LxdBackup,
    LxdBackupSource,
    LxdBackupDestination,
)
from lxdbackup.job import Job

from lxdbackup.zfs import ZfsUtil
from lxdbackup.backup_commands import ArgBuilder, SyncoidArgs, CommandRunner
from lxdbackup.backup_logs import Log
from lxdbackup.copy_params import CopyParams

from config.base_config import BackupConfig


CONFIG_FILENAME = ".config.yml"


def main():

    # Get an instance of Backup
    backup = get_backup()
    # get jobs from Backup
    jobs, _ = get_jobs(backup)

    # job runner
    for job in jobs:
        run_job(job)


# job runner
def run_job(job):
    for container in job["containers"]:
        container_copy_params = get_container_copy_params(job, container)
        # send to backup pipeline
        send_container_to_backup(container_copy_params)


def send_container_to_backup(container_copy_params):
    z_src, z_dst = src_dst_creator(container_copy_params)

    args = build_args(z_src, z_dst)
    cmd = ArgBuilder(args=args)
    run = CommandRunner(cmd.arg_string)

    do_backup(run)


def src_dst_creator(copy_params):
    z_src = setup_source(copy_params)
    z_dst = setup_dest(copy_params)
    return z_src, z_dst


# Job(BackupConfig)
# Factory?
def get_backup():
    return BackupConfig(CONFIG_FILENAME)


def get_jobs(backup):
    job = Job(backup)
    return job.jobs, job.job_containers


# ParamBuilder
# factory?
def get_container_copy_params(job, container):
    copy_params = CopyParams(
        src_container=container["name"],
        src_host=job["src_host"],
        src_host_user=job["src_user"],
        dst_container=container["dst_name"],
        dst_host=job["dst_host"],
        dst_host_user=job["dst_user"],
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


# Runner
def do_backup(run):
    result = asyncio.run(run.backup())


# logger
def logging(run):
    log = Log()
    log.log(run.result["stdout"], run.result["stderr"])


# param builder
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


# job setup
# todo fix why no source container path set
def setup_dest(copy_params):
    z_dst = ZfsUtil(host=copy_params.src_host, user=copy_params.src_host_user)
    z_dst.set_destination_container(copy_params.dst_container)
    return z_dst


# job setup
def setup_source(copy_params):
    z_src = ZfsUtil(host=copy_params.dst_host, user=copy_params.dst_host_user)
    z_src.set_source_container(copy_params.src_container)
    return z_src


if __name__ == "__main__":
    main()
