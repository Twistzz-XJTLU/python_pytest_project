"""
Built-in validate comparators.
"""
import re

import jsonpath


def equals(check_value, expect_value):
    assert check_value == expect_value, f'{check_value} == {expect_value}'


def less_than(check_value, expect_value):
    assert check_value < expect_value, f'{check_value} < {expect_value})'


def less_than_or_equals(check_value, expect_value):
    assert check_value <= expect_value, f'{check_value} <= {expect_value})'


def greater_than(check_value, expect_value):
    assert check_value > expect_value, f'{check_value} > {expect_value})'


def greater_than_or_equals(check_value, expect_value):
    assert check_value >= expect_value, f'{check_value} >= {expect_value})'


def not_equals(check_value, expect_value):
    assert check_value != expect_value, f'{check_value} != {expect_value})'


def string_equals(check_value, expect_value):
    assert str(check_value) == str(expect_value), f'{check_value} == {expect_value})'


def length_equals(check_value, expect_value):
    expect_len = _cast_to_int(expect_value)
    assert len(check_value) == expect_len, f'{len(check_value)} == {expect_value})'


def length_greater_than(check_value, expect_value):
    expect_len = _cast_to_int(expect_value)
    assert len(check_value) > expect_len, f'{len(check_value)} > {expect_value})'


def length_greater_than_or_equals(check_value, expect_value):
    expect_len = _cast_to_int(expect_value)
    assert len(check_value) >= expect_len, f'{len(check_value)} >= {expect_value})'


def length_less_than(check_value, expect_value):
    expect_len = _cast_to_int(expect_value)
    assert len(check_value) < expect_len, f'{len(check_value)} < {expect_value})'


def length_less_than_or_equals(check_value, expect_value):
    expect_len = _cast_to_int(expect_value)
    assert len(check_value) <= expect_len, f'{len(check_value)} <= {expect_value})'


def contains(check_value, expect_value):
    assert isinstance(check_value, (list, tuple, dict, str))
    assert expect_value in check_value, f'{len(expect_value)} in {check_value})'


def contained_by(check_value, expect_value):
    assert isinstance(expect_value, (list, tuple, dict, str))
    assert check_value in expect_value, f'{len(check_value)} in {expect_value})'


def regex_match(check_value, expect_value):
    assert isinstance(expect_value, str)
    assert isinstance(check_value, str)
    assert re.match(expect_value, check_value)


def startswith(check_value, expect_value):
    assert str(check_value).startswith(str(expect_value)), f'{str(check_value)} startswith {str(expect_value)})'


def endswith(check_value, expect_value):
    assert str(check_value).endswith(str(expect_value)), f'{str(check_value)} endswith {str(expect_value)})'


def _cast_to_int(expect_value):
    try:
        return int(expect_value)
    except Exception:
        raise AssertionError(f"%{expect_value} can't cast to int")


def extract_by_jsonpath(extract_value: dict, extract_expression: str):  # noqa
    """
        json path 取值
    :param extract_value: response.json()
    :param extract_expression: eg: '$.code'
    :return: None或 提取的第一个值 或全部
    """
    if not isinstance(extract_expression, str):
        return extract_expression
    extract_value = jsonpath.jsonpath(extract_value, extract_expression)
    if not extract_value:
        return
    elif len(extract_value) == 1:
        return extract_value[0]
    else:
        return extract_value


def extract_by_object(response, extract_expression):
    """
       从response 对象属性取值 [status_code, url, ok, headers, cookies, text, json, encoding]
    :param response: Response Obj
    :param extract_expression: 取值表达式
    :return: 返回取值后的结果
    """
    if extract_expression.startswith('$.'):
        response_parse_dict = response.json()
        return extract_by_jsonpath(response_parse_dict, extract_expression)
    else:
        # 其它非取值表达式，直接返回
        return extract_expression


def validate_response(response, validate_check) :
    """校验结果"""
    for check in validate_check:
        for check_type, check_value in check.items():
            actual_value = extract_by_jsonpath(response, check_value[0])  # 实际结果
            expect_value = check_value[1]  # 期望结果
            if check_type in ["eq", "equals", "equal"]:
                equals(actual_value, expect_value)
            elif check_type in ["lt", "less_than"]:
                less_than(actual_value, expect_value)
            elif check_type in ["le", "less_or_equals"]:
                less_than_or_equals(actual_value, expect_value)
            elif check_type in ["gt", "greater_than"]:
                greater_than(actual_value, expect_value)
            elif check_type in ["ne", "not_equal"]:
                not_equals(actual_value, expect_value)
            elif check_type in ["str_eq", "string_equals"]:
                string_equals(actual_value, expect_value)
            elif check_type in ["len_eq", "length_equal"]:
                length_equals(actual_value, expect_value)
            elif check_type in ["len_gt", "length_greater_than"]:
                length_greater_than(actual_value, expect_value)
            elif check_type in ["len_ge", "length_greater_or_equals"]:
                length_greater_than_or_equals(actual_value, expect_value)
            elif check_type in ["len_lt", "length_less_than"]:
                length_less_than(actual_value, expect_value)
            elif check_type in ["len_le", "length_less_or_equals"]:
                length_less_than_or_equals(actual_value, expect_value)
            elif check_type in ["contains"]:
                contains(actual_value, expect_value)
            else:
                print(f'{check_type}  not valid check type')
