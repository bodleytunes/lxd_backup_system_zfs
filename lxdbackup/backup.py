from abc import ABC, abstractmethod
import subprocess
from typing import Any, Container, List
from pydantic import BaseModel

from lxdbackup.connection import Connection


class Command(ABC):
    command_type = None

    @abstractmethod
    def run_command(
        self,
        conn: Connection,
        command=None,
    ):
        command.run_command(conn=conn)


class Container(BaseModel):

    name: str = None
    started: bool = None


class Orchestrator(ABC):
    @abstractmethod
    def _get_all_containers():
        pass

    @abstractmethod
    def list_containers():
        pass


class Lxd(Orchestrator):

    containers: List[Container]
    command: Command
    conn: Connection

    def __init__(self, conn: Connection) -> None:
        # self.run = Command()
        self.conn = conn
        # self.containers = self._get_all_containers()

    def _get_all_containers(self):
        # run command to get list of all containers
        return self.command.run_command(conn=self.conn)

    def list_containers(self):
        container_list = self.command.run_command(
            command=ListLxdCommand(), conn=self.conn
        )
        return self.command.run

    def run(self, cmd: Command):
        return cmd.run_command(conn=self.conn)


class ListLxdCommand(Command):
    OUTPUT_TYPE = "--output json"

    def __init__(self) -> None:
        pass

    def run_command(self, conn: Connection):
        #! todo fix this why no output
        stdin, stdout, stderr = conn.conn.exec_command(f"lxc list {self.OUTPUT_TYPE}")
        output = stdout.readlines()

        return output

    def json_to_dict(self, json_output):

        return json_output.__dict__


class ListNetworksLxdCommand(Command):
    OUTPUT_TYPE = "--output json"

    def __init__(self) -> None:
        pass

    def run_command(self, conn: Connection):
        stdin, stdout, stderr = conn.conn.exec_command(
            f"lxc network list {self.OUTPUT_TYPE}"
        )
        output = stdout.readlines()

        return output


class BackupLxdCommand(Command):
    OUTPUT_TYPE = "--output json"
    container_list: list

    def __init__(self) -> None:
        pass

    def run_command(self, conn: Connection):
        stdin, stdout, stderr = conn.conn.exec_command(
            f"zfs send | pigz | backup.tar.gz"
        )
        output = stdout.readlines()

        return output


class BackupObject:

    dst_folder: str

    def __init__(self) -> None:
        pass


class BackupLxdCommand(Command):

    container_backup_list: List[Container] = None

    def backup():
        pass


class Server:

    # conn: Connection
    lxd: Orchestrator

    def __init__(self, lxd: Orchestrator) -> None:
        # self.conn = conn
        self.lxd = lxd
