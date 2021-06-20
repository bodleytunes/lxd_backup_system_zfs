from abc import ABC, abstractmethod
import subprocess
from typing import Any, Container, List
from pydantic import BaseModel

from lxdbackup.connection import Connection


class Command:
    command_type = None

    def __init__(self) -> None:
        super().__init__()

    def run_command(self, command=None):
        command.run_command()


class Container(BaseModel):

    name: str = None
    started: bool = None


class Lxd(ABC):

    containers: List[Container]
    command: Command

    def __init__(self) -> None:
        super().__init__()
        self.command = Command()
        self.containers = self._get_all_containers()

    def _get_all_containers(self):
        # run command to get list of all containers
        return self.command.run_command(command=ListLxdCommand())

    # def list_containers(self)


class ListLxdCommand(Command):
    OUTPUT_TYPE = "--output json"

    def __init__(self) -> None:
        super().__init__()

    def run_command(self):
        output = subprocess.run(f"lxc list {self.OUTPUT_TYPE}")
        # json_output = print(f"lxc list --output json")
        print(output)

        return output

    def json_to_dict(self, json_output):

        return json_output.__dict__


class BackupLxdCommand(Command):

    container_backup_list: List[Container] = None

    def backup():
        pass


class Server:

    conn: Connection = None
    lxd: Lxd = None

    def __init__(self, conn: Connection) -> None:
        self.lxd = self._get_lxd_instance()
        self.conn = conn

    def _get_lxd_instance(self):
        self.lxd = Lxd()
