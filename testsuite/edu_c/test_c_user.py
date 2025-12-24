import allure

from api.c_user_api import ClientUserApi


@allure.feature("c小程序用户中心")
class Test_c_user(object):

    @allure.story("获取职位列表")
    @allure.title("获取职位列表")
    def test_get_position_list(self):
        result = ClientUserApi().get_position_list(None)
        assert result["code"] == 200

    @allure.story("获取职位详情")
    @allure.title("获取职位详情")
    def test_get_position_detail(self):
        result = ClientUserApi().get_position_detail(None)
        assert result["code"] == 200

    @allure.story("获取首页底部配置")
    @allure.title("获取首页底部配置")
    def test_get_bottom_menu_configuration(self):
        result = ClientUserApi().get_bottom_menu_configuration(None)
        assert result["code"] == 200

