import json

from core.api_util import api_util

# A方法
from utils.log_util import logger
from utils.response_util import process_response


def mobile_query(params):
    response = api_util.get_mobile_belong(params=params)
    result = process_response(response)

    return result


def test_json(json_data):
    """
    这个方法测试json传参
    :param json_data:
    :return:
    """
    response = api_util.post_data(json=json_data)
    process_response(response)
    return response.json()
