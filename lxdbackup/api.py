from abc import ABC

from pylxd import Client


class FactoryLxdApi:
    @staticmethod
    def get_lxd_api_client(connect_args: ConnectArgs):
        c = Client(endpoint=endpoint, cert=(cert, key), verify=False)
        return c


class Api(ABC):
    pass


class LxdApi(Api):

    api_command: ApiCommand()

    def connect():
        pass


class ApiCommand:
    pass

    def list_containers():
        pass

    def list_networks():
        pass

    def backup_containers():
        pass


# lxdapi.connect()
# lxdapi.api_command(LxcListCommand())
