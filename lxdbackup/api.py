from abc import ABC


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
