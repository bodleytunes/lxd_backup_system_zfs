from typing import Any, Optional
import paramiko
from pydantic import basemodel
from paramiko import channel, client

class ConnectArgs(basemodel):
    hostname: str = None
    username: str = None
    password: str = None
    
    def __init__(self, hostname: str, username: str, password: str) -> None:
        self.hostname = hostname
        self.username = username
        self.password = password
    

class FactoryConnection():

    def get_paramiko_connection():
        conn = client.SSHClient.connect(hostname="blah", port="foo")

class Connection(connect_args: ConnectArgs, conn: Any)