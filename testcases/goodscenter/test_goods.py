import allure

from api.goods_api import get_banner


@allure.feature("用户中心模块")
class TestGoods:
    @allure.story("首页展示内容")
    @allure.title("banner")
    def test_banner(self, banner_num):
        result = get_banner()
        assert result.success is True
        assert len(result.body) == banner_num
