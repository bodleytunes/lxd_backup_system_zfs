from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, time, timedelta
import subprocess
from typing import Any, Container, List
from pydantic import BaseModel
from pydantic.errors import DataclassTypeError
import confuse
from pylxd import Client as Api


from lxdbackup.connection import Connection


# todo new stuff
@dataclass
class LxdBackupSource:

    backup_source_host: str
    selected_backup_source_dataset: str


@dataclass
class LxdBackupDestination:

    backup_destination_host: str
    selected_backup_destination_dataset: str


class LxdBackup:
    src_host: str
    dst_host: str
    backup_source: LxdBackupSource
    backup_destination: LxdBackupDestination
    backup_command = None

    def set_backup_src(self, src: LxdBackupSource):
        self.backup_source = src
        pass

    def set_backup_dst(self, dst: LxdBackupDestination):
        self.backup_destination = dst
        pass

    def run_backup():
        pass
