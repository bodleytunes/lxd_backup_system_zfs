from pydantic.main import BaseConfig
from lxdbackup import backup, connection
from config.base_config import BaseConfig


def main():
    creds = BaseConfig.get_creds(filename=".creds.yml")
    connect_args = connection.ConnectArgs(
        hostname="10.55.0.66", username="root", password=creds
    )
    paramiko_conn = connection.FactoryConnection.get_paramiko_connection(connect_args)
    conn = connection.Connection(conn=paramiko_conn)


if __name__ == "__main__":
    main()
