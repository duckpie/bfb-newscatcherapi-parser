from src.config import Config_Parser


class Parser:
    def __init__(self, parser_cfg: Config_Parser) -> None:
        self.__parser_cfg = parser_cfg

    def get_data(self):
        print("test11")
