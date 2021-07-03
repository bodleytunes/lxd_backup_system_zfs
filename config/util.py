from dataclasses import dataclass

from abc import ABC


class CmdArgs:
    pass


@dataclass
class SyncoidArgs(CmdArgs):
    cmd = "syncoid"
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
            f"{self.syncoid_args.cmd} {self.syncoid_args.src_dataset}{self.syncoid_args.src_mid}{self.syncoid_args.container}"
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

        pass

    def backup(self):
        pass
        # cmd process run
        # run self.arg_string
