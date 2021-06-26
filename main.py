from typing import List
from pylxd import Client

from lxdbackup.backup import (
    BackupLxdCommand,
    ListNetworksLxdCommand,
    ListLxdCommand,
    Orchestrator,
    Lxd,
    Server,
    BackupParams,
    BackupArchive,
)

from pydantic.main import BaseConfig
import confuse
from lxdbackup import backup, connection
from config.base_config import BaseConfig, ConfigItem

FILENAME = ".config.yml"


def main():
    # lxd_client = Client()
    get_base_config()
    username, password, hostname = get_credentials()
    connect_args = get_connect_args(username, password, hostname)
    paramiko = connection.FactoryConnection.get_paramiko_connection(connect_args)
    conn = connection.Connection(conn=paramiko)
    # todo
    lxd = Lxd(conn=conn)
    server = Server(lxd=lxd)

    # run a list lxd containers command
    container_list = server.lxd.run(ListLxdCommand())
    # run a list lxd networks command
    network_list = server.lxd.run(ListNetworksLxdCommand())
    # run a container backup command #! todo
    backup_result = server.lxd.run(
        BackupLxdCommand(BackupParams(dst_folder="/tmp", start_time="now"))
    )
    # container_list = server.lxd.command.list_containers()
    # result: BackupResult = server.lxd.command.backup_all_running_containers(
    #    containers=container_list
    # )


def get_base_config():
    """
    config = BaseConfig().get_config_item(
        FILENAME, ConfigItem(item="username", config_file=FILENAME)
    )
    """
    config = confuse.Configuration("lxdbackup", __name__)
    config.set_file(".config.yml")
    print(config["lxd"].get())
    print(config["lxd"]["api"]["auth"]["cert"].get())


def get_connect_args(username, password, hostname):
    connect_args = connection.ConnectArgs(
        hostname=hostname, username=username, password=password
    )
    return connect_args


def get_credentials():
    username = BaseConfig.get_username(filename=FILENAME)
    password = BaseConfig.get_password(filename=FILENAME)
    hostname = BaseConfig.get_hostname(filename=FILENAME)
    return username, password, hostname


if __name__ == "__main__":
    main()
