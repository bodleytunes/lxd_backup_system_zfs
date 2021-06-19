from lxdbackup import backup, connection


def main():
    print("do something")
    connect_args = connection.ConnectArgs(
        hostname="10.55.0.66", username="root", password="bailey"
    )
    paramiko_conn = connection.FactoryConnection.get_paramiko_connection(connect_args)
    conn = connection.Connection(conn=paramiko_conn)


if __name__ == "__main__":
    main()
