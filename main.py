import os
import redis

from src.config import Config
from src.parser.newscatcher_parser import Parser


if __name__ == '__main__':
    cfg = Config(os.environ['ENV'])

    r = redis.Redis(
        host=cfg.get_services().get_redis().get_host(),
        port=cfg.get_services().get_redis().get_port(),
        db=cfg.get_services().get_redis().get_db()
    )

    query = {
        "q": "Россия OR Украина OR Белоруссия",
        "lang": "ru",
        "sort_by": "relevancy",
        "page": "1",
        "page_size": "100"
    }

    parser = Parser(cfg.get_services().get_parser(), r, query)
    parser.get_data()
