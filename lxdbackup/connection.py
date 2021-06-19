from typing import Any, Optional
import paramiko
from pydantic import BaseModel
from paramiko import channel, client


class ConnectArgs(BaseModel):
    hostname: str = None
    username: str = None
    password: str = None


class FactoryConnection:
    @staticmethod
    def get_paramiko_connection(connect_args: ConnectArgs):
        c = client.SSHClient()
        c.load_system_host_keys()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        c.connect(hostname=connect_args.hostname)
        return c


class Connection:
    def __init__(self, conn: client.SSHClient) -> None:
        self.conn = conn

        pass
