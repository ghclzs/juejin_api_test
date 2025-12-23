import copy

from base_client.client import RestClient
from config.config import config


class ClientUserApi:
    def __init__(self):
        self.url = config.prod_c_uniapp_url



    def get_position_list(self, token):
        headers = copy.deepcopy(config.C_uniappBaseHeader)
        headers['Blade-Auth'] = token
        url = self.url + "/edu-pm/v1/applet/position/get-list?size=30&current=1&isSearch=false&searchTab=RECOMMENDED&location=113.423305%2C23.100007&ttgId=&positionIds="
        result = RestClient().do_request(method="GET", url=url, headers=headers, json=None)
        return result

    def get_position_detail(self, token):
        headers = copy.deepcopy(config.C_uniappBaseHeader)
        headers['Blade-Auth'] = token
        url = self.url + "/edu-pm/v1/applet/position/get-detail?id=2003302443144683521&location=113.423305,23.100007"
        result = RestClient().do_request(method="GET", url=url, headers=headers, json=None)
        return result
