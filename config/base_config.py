import yaml
import os


class BaseConfig:
    @staticmethod
    def get_username(filename):

        if os.getenv("USERNAME") is not None:
            username = os.environ.get("USERNAME")
        else:
            creds = BaseConfig._get_file(filename)
            username = creds["credentials"]["username"]

        return username

    @staticmethod
    def get_password(filename):

        if os.getenv("PASSWORD") is not None:
            PASSWORD = os.environ.get("PASSWORD")
        else:
            creds = BaseConfig._get_file(filename)

            PASSWORD = creds["credentials"]["password"]

        return PASSWORD

    @staticmethod
    def get_password(filename):

        if os.getenv("HOSTNAME") is not None:
            HOSTNAME = os.environ.get("HOSTNAME")
        else:
            creds = BaseConfig._get_file(filename)

            HOSTNAME = creds["credentials"]["hostname"]

        return HOSTNAME

    @staticmethod
    def _get_file(filename):

        with open(filename) as file:
            creds = yaml.load(file, Loader=yaml.FullLoader)

        return creds
