import json
import requests

from src.config import Config_Parser


class Parser:
    def __init__(self, cfg: Config_Parser, redis, query: str) -> None:
        self.__cfg = cfg
        self.query = query
        self.current_proxy = self.__cfg.get_proxies()[0]
        self.connection_attempts = 0
        self.redis = redis

    def get_data(self):
        try:
            resp = requests.get(
                "https://{0}/v2/search".format(self.__cfg.get_host()),
                proxies={
                    'https': self.current_proxy
                },
                headers={
                    "x-api-key": self.__cfg.get_token()
                },
                params=self.query,
                timeout=60
            )

            self.save_data(json.loads(resp.text))
        except requests.exceptions.Timeout:
            # Если сработал таймаут, вероятно прокси перестал работать.
            # Чтобы точно убедиться, позволяю еще раз воспользоваться этим прокси.
            # И если повторные попытки так же не успешны, меняю текущий прокси.

            self.connection_attempts += 1
            if self.connection_attempts >= 2:
                i = self.__cfg.get_proxies().index(self.current_proxy)
                if len(self.__cfg.get_proxies()) == i:
                    self.current_proxy = self.__cfg.get_proxies()[0]
                    # TODO: добавить уведомление о том, что все прокси не отвечают
                else:
                    self.current_proxy = self.__cfg.get_proxies()[i+1]

        except requests.exceptions.RequestException as e:
            pass

    def save_data(self, data):
        for item in data['articles']:
            obj = {
                "title": item['title'],
                "country":  item['country'],
                "language":  item['language'],
                "rights": item['rights'],
                "clean_url": item['clean_url'],
            }

            self.redis.set(item['_id'], json.dumps(obj))
