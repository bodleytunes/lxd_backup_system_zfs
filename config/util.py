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
        cmd: str = args.cmd
        src_dataset: str = args.src_dataset
        src_mid: str = args.src_mid
        container: str = args.container
        user: str = args.user
        dst_host: str = args.dst_host
        dst_dataset: str = args.dst_dataset
        dst_mid: str = args.dst_mid
        dst_container: str = args.dst_container
        mbuffer_size: int = args.mbuffer_size
        pv_options: str = args.pv_options
        compression: str = args.compression
        other_opts: str = args.other_opts

        arg_string: str = self._build_args

        pass

    def _build_args(self):

        return str(f"{self.cmd}{self.src_dataset}")
