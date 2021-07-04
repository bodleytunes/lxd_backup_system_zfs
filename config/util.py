from dataclasses import dataclass

from abc import ABC
from typing import Any, List

from zfslib import zfslib as zfs


class CmdArgs:
    pass


@dataclass
class ZfsDataset:
    full_path: str
    split_path: list


@dataclass
class ZfsPool:
    name: str
    zfs_datasets: List[ZfsDataset]


@dataclass
class ZfsDetails:
    host: str
    zfs_pools: List[ZfsPool]


class ZfsUtil:
    def __init__(self, host: str) -> None:
        self.host = host
        self._get_conn()
        self._get_poolset()

        self.datasets: List = list()
        pass

    def _get_conn(self):
        self.conn = zfs.Connection(host=self.host)

    def _get_poolset(self):
        self.poolset = self.conn.load_poolset()

    def get_pool_names(self):
        for p in self.poolset:
            print(p.name)

    def get_pool_datasets(self):
        for p in self.poolset:
            self.datasets.append(p.get_all_datasets())
        pass


@dataclass
class SyncoidArgs(CmdArgs):
    CMD = "syncoid"
    src_dataset = "zpool1"
    src_mid = "/containers/"
    container = "gitea"
    user = "root"
    dst_host = "p21"
    dst_dataset = "zpool1"
    dst_mid = "/lxd/containers"
    dst_container = "gitea"
    mbuffer_size = 128
    pv_options = "-b"
    compression = "zstd-fast"
    other_opts = "--no-stream --no-sync-snap --debug"


class ArgBuilder:
    """
    syncoid zpool1/containers/gitea root@p21:zpool1/lxd/containers/gitea --mbuffer-size=128M --pv-options=-b --no-stream --no-sync-snap --compress=zstd-fast --debug
    """

    def __init__(self, args: SyncoidArgs) -> None:

        self.syncoid_args: SyncoidArgs = args
        self.src: str = self._build_src()
        self.dst: str = self._build_dst()
        self.params: str = self._build_params()
        self.arg_string: str = self._build_args()

        pass

    def _build_src(self):
        return str(
            f"{self.syncoid_args.CMD} {self.syncoid_args.src_dataset}{self.syncoid_args.src_mid}{self.syncoid_args.container}"
        )

    def _build_dst(self):
        return str(
            f"{self.syncoid_args.user}@{self.syncoid_args.dst_host}:{self.syncoid_args.dst_dataset}{self.syncoid_args.dst_mid}/{self.syncoid_args.dst_container}"
        )

    def _build_params(self):
        return str(
            f"--mbuffer-size={self.syncoid_args.mbuffer_size}M --pv-options={self.syncoid_args.pv_options} --compress={self.syncoid_args.compression} {self.syncoid_args.other_opts}"
        )

    def _build_args(self):
        return str(f"{self.src} {self.dst} {self.params}")


class CommandRunner:
    def __init__(self, arg_string: str) -> None:

        self.arg_string = arg_string
        self.log_output

        pass

    def backup(self):
        pass
        # cmd process run
        # run self.arg_string