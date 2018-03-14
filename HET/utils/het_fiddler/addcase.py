import os
import time
import json
from utils.het_fiddler.util._myrequests import _requests, _sign, _myMD5, _search, _newsearch
HOST = "http://200.200.200.230"
APPSECRET = "bf1f3ce24b304af3ab7971aaec318135"
HEADERS = {"Content-type": "application/x-www-form-urlencoded", 'Accept': '*/*'}


RESULTDIR = os.path.join(os.getcwd(),'utils/het_fiddler/datas/result/result.txt')
def addcase(appid, except_code, url_type, http_type, host, url_name, url_remark, case_name, body):
    method = "POST"
    url = "{_host}/task/case/add".format(_host=HOST)
    arg = {
        "app_id": appid,
        "url_type": url_type,
        "http_type": http_type,
        "host": host,
        "url_name": "/" + url_name,
        "url_remark": url_remark,
        "case_name": case_name + "|",
        "body": body + "||",
        "except_code": except_code
    }
    result = _requests(url, arg, HEADERS)
    if except_code in ['accessToken', 'accessTokenExpires', 'refreshToken', 'refreshTokenExpires']:
        url = "{_host}/task/relation/add".format(_host=HOST)
        arg = {
            "app_id": appid,
            "case_id": result.json().get('case_id', None),
            "relation_name": 'accessToken_%s' % appid,
            "source": 1,
            "left": 'accessToken":"',
            "right": "'"
        }
        _requests(url, arg, HEADERS)
    return result.text


def addcase_main():
    with open(RESULTDIR, "r", encoding='UTF-8') as f:
        url = {}
        for eachline in f:
            (casename, method, version, protocol, host, path,
             forms, isurl, isparams, code, message, rspbody) = eachline.strip().split("                    ")
            for k, v in json.loads(rspbody).items():
                if isinstance(v, dict):
                    except_code = v.popitem()[0]
                else:
                    except_code = '"code":0'
            appid = json.loads(forms).get('appId', None)
            url[path] = (
            appid, except_code, casename, method, version, protocol, host, path, forms, isurl, isparams, code, message,
            rspbody)
        for z, w in url.items():
            (appid, except_code, method, protocol, host, path, casename, casename, forms) = w[0], w[1], w[3], w[5], w[
                6], w[7], w[7].split('/')[-1], w[7].split('/')[-1], w[8]
            try:
                addcase(appid, except_code, method, protocol, host, path, casename, casename, forms)
                time.sleep(0.05)
            except:
                continue
    return



