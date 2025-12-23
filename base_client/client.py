
# -*- coding: utf-8 -*-
import json

import pytest
import requests
import time
# from common.robot import Robot
# from config.config import config
# from config.dev_sql_operate import MysqlOperate_dev
# from robot.Robot import Robot
from log.log import logger
from requests_toolbelt import MultipartEncoder  # 新增导入 MultipartEncoder 类


class RestClient:
    def __init__(self):
        self.session = requests.Session()
        # self.sql_operate = MysqlOperate_dev()


    def do_request(self, url, method,type=None, **kwargs):
        data = dict(**kwargs).get("data")
        json_data = dict(**kwargs).get("json")
        params = dict(**kwargs).get("params")
        headers = dict(**kwargs).get("headers")

        # 新增：检查是否是 MultipartEncoder 对象
        if isinstance(data, MultipartEncoder):
            headers['Content-Type'] = data.content_type

        if data is not None:
            request_data = data
        elif params is not None:
            request_data = params
        elif json_data is not None:
            request_data = json_data
        else:
            request_data=None

        if type == "excel":
            # 如果是文件类型响应，返回原始响应对象
            start_time = time.time()
            response = self.request(url, method, **kwargs)
            end_time = time.time()
            response_duration_time = end_time - start_time
            logger.info("接口返回内容>>>\n{}".format(response.content[:100]))  # 打印前100个字符查看文件头
            logger.info("接口响应时间>>>:{}".format(response_duration_time))
            return response  # 直接返回响应对象
        else:
            start_time = time.time()
            response = self.request(url, method, **kwargs).json()
            end_time = time.time()
            response_duration_time = end_time - start_time
            logger.info("接口返回内容>>>\n{}".format(json.dumps(response, ensure_ascii=False, indent=2)))
            logger.info("接口响应时间>>>:{}".format(json.dumps(response_duration_time, ensure_ascii=False, indent=2)))
            # if 'code' not in response or response['code'] != 200:
            #     sql_data = (url, method, json.dumps(headers, ensure_ascii=False), json.dumps(request_data, ensure_ascii=False),
            #     response.get('code'), json.dumps(response, ensure_ascii=False), str(response_duration_time))
            #     sql = "insert api_test_db.api_test_results(api_url,request_method,request_headers,request_data,response_status_code,response_data,response_duration_time)VALUES (%s,%s,%s,%s,%s,%s,%s)"
            #     # self.sql_operate.insert_update_table(sql, sql_data)


        return response

    def request(self, url, method, **kwargs):

        self.request_log(url, method, **kwargs)
        if method == "GET":
            return self.session.get( url, **kwargs)
        if method == "POST":
            return self.session.post( url, **kwargs)
        if method == "PUT":
            return self.session.put(  url, **kwargs)
        if method == "DELETE":
            return self.session.delete(  url, **kwargs)

    #打印接口参数log日志
    def request_log(self, url, method, **kwargs):
        data = dict(**kwargs).get("data")
        json_data = dict(**kwargs).get("json")
        params = dict(**kwargs).get("params")
        headers = dict(**kwargs).get("headers")

        logger.info("接口请求的地址>>>{}".format(url))
        logger.info("接口请求的方法>>>{}".format(method))
        if headers is not None:
            logger.info("接口请求的headers参数>>>\n{}".format(json.dumps(headers, ensure_ascii=False, indent=2)))
        if data is not None:
            # 新增：检查是否是 MultipartEncoder 对象
            if isinstance(data, MultipartEncoder):
                logger.info("接口请求的data参数是 MultipartEncoder 类型")
            else:
                logger.info("接口请求的data参数>>>\n{}".format(json.dumps(data, ensure_ascii=False, indent=2)))
        if json_data is not None:
            logger.info("接口请求的json参数>>>\n{}".format(json.dumps(json_data, ensure_ascii=False, indent=2)))
        if params is not None:
            logger.info("接口请求的params参数>>>\n{}".format(json.dumps(params, ensure_ascii=False, indent=2)))




