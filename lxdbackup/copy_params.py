from dataclasses import dataclass


@dataclass
class CopyParams:
    src_host: str
    src_host_user: str
    src_container: str
    dst_host: str
    dst_host_user: str
    dst_container: str
