from abc import ABC, abstractmethod
import subprocess
from typing import Any, Container, List
from pydantic import BaseModel

from lxdbackup.connection import Connection


class Command:
    command_type = None

    def __init__(self) -> None:
        super().__init__()

    def run_command(
        self,
        conn: Connection,
        command=None,
    ):
        command.run_command(conn=conn)


class Container(BaseModel):

    name: str = None
    started: bool = None


class Lxd:

    containers: List[Container]
    command: Command
    conn: Connection

    def __init__(self, conn: Connection) -> None:
        super().__init__()
        self.command = Command()
        self.conn = conn
        self.containers = self._get_all_containers()

    def _get_all_containers(self):
        # run command to get list of all containers
        return self.command.run_command(command=ListLxdCommand(), conn=self.conn)

    def list_containers(self):
        container_list = self.command.run_command(
            command=ListLxdCommand(), conn=self.conn
        )
        return self.command.run


class ListLxdCommand(Command):
    OUTPUT_TYPE = "--output json"

    def __init__(self) -> None:
        super().__init__()

    def run_command(self, conn: Connection):
        #! todo fix this why no output
        stdin, stdout, stderr = conn.conn.exec_command("ls -lahst")
        output = stdout.readlines()

        return output

    def json_to_dict(self, json_output):

        return json_output.__dict__


class BackupLxdCommand(Command):

    container_backup_list: List[Container] = None

    def backup():
        pass


class Server:

    conn: Connection
    lxd: Lxd

    def __init__(self, conn: Connection, lxd: Lxd) -> None:
        self.conn = conn
        self.lxd = Lxd(conn=self.conn)
