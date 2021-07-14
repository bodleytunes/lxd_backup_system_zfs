from dataclasses import dataclass
from typing import Optional

import subprocess


class CmdArgs:
    pass


@dataclass
class SyncoidArgs(CmdArgs):
    CMD: str = "/usr/sbin/syncoid"

    src_user: str = "root"
    dst_user: str = "root"
    src_host: str = "p21"
    dst_host: str = "p21"

    zfs_source_path: Optional[str] = None
    zfs_destination_path: Optional[str] = None

    mbuffer_size: int = 128
    pv_options: str = "-b"
    compression: str = "zstd-fast"
    other_opts: str = "--no-stream --debug"


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
            f"{self.syncoid_args.CMD} {self.syncoid_args.src_user}@{self.syncoid_args.src_host}:{self.syncoid_args.zfs_source_path}"
        )

    def _build_dst(self):
        return str(
            f"{self.syncoid_args.dst_user}@{self.syncoid_args.dst_host}:{self.syncoid_args.zfs_destination_path}"
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
        self._create_process()

        pass

    def _create_process(self) -> None:
        self.process = subprocess.Popen(
            self.arg_string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

    def backup(self) -> dict:
        out, err = self.process.communicate()
        self.result = {"stdout": out, "stderr": err}
