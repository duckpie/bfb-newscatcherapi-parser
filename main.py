import argparse

from src.config import Config
from src.parser.newscatcher_parser import Parser


def init():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--env", help="Working environment",
                        type=str, default="local")

    return parser.parse_args()


if __name__ == '__main__':
    args = init()

    cfg = Config(args.env)
    parser = Parser(cfg.get_services().get_parser())

    parser.get_data()
