from pydantic.main import BaseConfig
from lxdbackup import backup, connection
from config.base_config import BaseConfig

FILENAME = ".creds.yml"


def main():
    username, password = get_credentials()
    connect_args = get_connect_args(username, password)
    paramiko = connection.FactoryConnection.get_paramiko_connection(connect_args)
    conn = connection.Connection(conn=paramiko)


def get_connect_args(username, password):
    connect_args = connection.ConnectArgs(
        hostname="10.55.0.66", username=username, password=password
    )
    return connect_args


def get_credentials():
    username = BaseConfig.get_username(filename=FILENAME)
    password = BaseConfig.get_password(filename=FILENAME)
    return username, password


if __name__ == "__main__":
    main()
