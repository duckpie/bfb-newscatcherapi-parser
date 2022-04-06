import os
import requests
import json
import redis

from src.config import Config
from src.parser.newscatcher_parser import Parser


if __name__ == '__main__':
    # cfg = Config(os.environ['ENV'])
    cfg = Config('local')

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

    parser = Parser(cfg.get_services().get_parser(), query)
    parser.get_data()

    # url = "https://api.newscatcherapi.com/v2/search"

    # headers = {
    #     "x-api-key": cfg.get_services().get_parser().get_token()
    # }

    # proxies = {
    #     'https': '14.17.106.202:3128'
    # }

    # response = requests.get(url,
    #                         proxies=proxies,
    #                         headers=headers,
    #                         params=querystring,
    #                         timeout=60,
    #                         )

    # data = json.loads(response.text)

    # for item in data['articles']:
    #     obj = {
    #         "title": item['title'],
    #         "country":  item['country'],
    #         "language":  item['language'],
    #         "rights": item['rights'],
    #         "clean_url": item['clean_url'],
    #     }
    #     r.set(item['_id'], json.dumps(obj))
