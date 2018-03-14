

from urllib.parse import unquote

from utils.het_fiddler.util.script import globalvalue
import re

def split_params(string):
    """将http请求中的参数串解析成字典返回

    :param string:  str
    """
    string = string[:-1] if string.endswith("&") else string
    params = [each.split("=") for each in string.split("&")]
    forms = {key:unquote(value) for key, value in params} if string else {}
    return forms

def dic_to_str(dic, symbol="|"):
    """使用分隔符，将字典拼接成字串

    :param dic: dic
    :param symbol:  分隔符
    """
    sortDic = sorted(dic.iteritems(),key = lambda d: d[0]) if dic else dic
    keystring = symbol.join(str(key) for key,value in sortDic) if sortDic else ""
    valuestring = symbol.join(str(value) for key,value in sortDic) if sortDic else ""
    return keystring,valuestring

def str_to_dic(keystring, valuestring, symbol="|"):
    """使用分隔符将字串分隔，并转成字典

    :param keystring:   键字串
    :param valuestring: 值字串
    :param symbol:  分隔符
    """
    keys = keystring.split(symbol) if keystring else keystring
    values = valuestring.split(symbol) if valuestring else valuestring
    result = {key:value for key,value in zip(keys,values)} if keys and values else {}
    return result

def search_url(path, symbol="|"):
    """查询URL中是否有特定URL

    :param path:
    :param symbol:  分隔符
    """
    params = globalvalue.URLS[path] if path in globalvalue.URLS.keys() else ""
    return symbol.join(each for each in params)

def search_params(forms, symbol="|"):
    """查询params中是否有特定参数

    :param forms:
    :param symbol:  分隔符
    """
    return symbol.join(each for each in globalvalue.PARAMS.keys() if each in forms.keys())

def get_params(string):
    for each in str_to_dic(string):
        pat = re.compile(globalvalue.PARAMS[each])
        result = pat.search(strting)
        key,value = result.split(":")
        globalvalue.DATAS[each] = value.strip('"')

def update_params(forms):
    for each in globalvalue.PARAMS.keys():
        forms[each] = globalvalue.DATAS[each]

if __name__=="__main__":
    string = "username=cusAdmin&password=ZTEwYWRjMzk0OWJhNTlhYmJlNTZlMDU3ZjIwZjg4M2U%3D&_=1518141218307"
