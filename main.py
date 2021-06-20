from pydantic.main import BaseConfig
from lxdbackup import backup, connection
from config.base_config import BaseConfig
import lxdbackup

FILENAME = ".creds.yml"
# hostname = "10.55.0.66"


def main():
    username, password, hostname = get_credentials()
    connect_args = get_connect_args(username, password)
    paramiko = connection.FactoryConnection.get_paramiko_connection(connect_args)
    conn = connection.Connection(conn=paramiko)
    # todo
    lxd = backup.Server(conn=conn)  # ! todo


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
