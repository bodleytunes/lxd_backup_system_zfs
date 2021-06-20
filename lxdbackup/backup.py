from abc import ABC, abstractmethod
from typing import Any, Container, List
from pydantic import BaseModel
from connection import Connection


class Lxd(ABC):

    containers: List[Container]

    def __init__(self) -> None:
        super().__init__()
        self.containers = self._get_all_containers()

    def _get_all_containers():
        # run command to get list of all containers
        command = ListLxdCommand()
        command.run_command()
        pass


class Command(ABC):
    @abstractmethod
    def run_command():
        pass


class ListLxdCommand(Command):
    def __init__(self) -> None:
        super().__init__()

    def run_command(self):
        json_output = print(f"lxc list --output json")

        dict_output = self.json_to_dict(json_output)

    def json_to_dict(self, json_output):

        return json_output.__dict__


class BackupLxdCommand(Command):

    container_backup_list: List[Container] = None

    def backup():
        pass


class Container(BaseModel):

    name: str = None
    started: bool = None


class Server:

    conn: Connection = None
    lxd: Lxd = None

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        self.lxd = self._get_lxd_instance()

    def _get_lxd_instance(self):
        self.lxd = Lxd()
