import requests

from src.config import Config_Parser


class Parser:
    def __init__(self, parser_cfg: Config_Parser, query: str) -> None:
        self.__parser_cfg = parser_cfg
        self.query = query

    def get_data(self):
        headers = {
            "x-api-key": self.__parser_cfg.get_services().get_parser().get_token()
        }

        response = requests.get(url,
                                proxies=proxies,
                                headers=headers,
                                params=querystring,
                                timeout=60,
                                )

        try:
            r = requests.get(url, params={'s': thing})
        except requests.exceptions.Timeout:
            pass
            # Maybe set up for a retry, or continue in a retry loop
        except requests.exceptions.TooManyRedirects:
            pass
            # Tell the user their URL was bad and try a different one
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            raise SystemExit(e)
