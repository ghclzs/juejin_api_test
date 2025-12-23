import copy
from urllib import parse

import pytest

from base_client.client import RestClient
from config.config import config





class ClientAccountApi:
    def __init__(self):
        self.url ="https://api.juejin.cn"

    def get_position_list(self):
        url = self.url + ""
        res = RestClient().do_request(method="GET",url=url, headers=config.BaseHeader)



