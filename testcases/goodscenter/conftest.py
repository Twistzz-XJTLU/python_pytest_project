import pytest

from utils.mysql_util import db


@pytest.fixture()
def banner_num():
    sql = "select count(1) as banner_num from goods_banner;"
    result = db.select_db_one(sql)
    return result['banner_num']
