import datetime
import os

import pytest
# from pytest_jsonreport.plugin import JSONReport



if __name__ == '__main__':
    # plugin = JSONReport()
    now = datetime.datetime.now()
    time_str = now.strftime("%Y-%m-%d-%H%M%S")
    current_directory = os.path.dirname(os.path.abspath(__file__))[:30]
    pytest.main(["-vs"])
    # 生成xml报告
    # pytest.main(["-p","pytest_wechat_notify","./testsuite/admin_operate/test_admin_operate_tag.py","--alluredir="+str(current_directory)+"\yushunResult\Report\{}xml ".format(time_str) ], plugins=[plugin])
    # pytest.main(["--alluredir=" + str(current_directory) + "\yushunResult\Report\{}xml".format(time_str),"-n","4"],plugins=[plugin])
    # # #此处命令 allure generate 将前面生成的json文件转换为html的报告
    # os.system("allure generate " + str(current_directory) + "\yushunResult\Report\{}xml".format(time_str) + " -o " + str(current_directory) + "\yushunResult\Report\{}html --clean ".format(time_str))




