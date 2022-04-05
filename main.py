import os

from src.config import Config
from src.parser.newscatcher_parser import Parser


if __name__ == '__main__':
    cfg = Config(os.environ['ENV'])
    parser = Parser(cfg.get_services().get_parser())

    parser.get_data()
