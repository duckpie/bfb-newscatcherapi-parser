import yaml


class Config_Parser:
    def __init__(self, parser_params: dict) -> None:
        self.__host = parser_params["host"]
        self.__token = parser_params["token"]

    def get_host(self) -> str:
        return self.__host

    def get_token(self) -> str:
        return self.__token


class Config_Server:
    def __init__(self, server_params: dict) -> None:
        self.__host = server_params["host"]
        self.__port = server_params["port"]

    def get_host(self) -> str:
        return self.__host

    def get_port(self) -> int:
        return self.__port


class Config_Redis:
    def __init__(self, redis_params: dict) -> None:
        self.__host = redis_params["host"]
        self.__port = redis_params["port"]
        self.__db = redis_params["db"]

    def get_host(self) -> str:
        return self.__host

    def get_port(self) -> int:
        return self.__port

    def get_db(self) -> int:
        return self.__db


class Config_Servicers:
    def __init__(self, services_params: dict) -> None:
        self.__parser = Config_Parser(services_params["parser"])
        self.__redis = Config_Redis(services_params["redis"])

    def get_parser(self) -> Config_Parser:
        return self.__parser

    def get_redis(self) -> Config_Redis:
        return self.__redis


class Config:
    def __init__(self, env: str) -> None:
        with open("config/config.{0}.yml".format(env)) as f:
            data = yaml.safe_load(f)
            self.__services = Config_Servicers(data["services"])

    def get_services(self) -> Config_Servicers:
        return self.__services
