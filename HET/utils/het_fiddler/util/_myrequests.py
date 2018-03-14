
import base64
import binascii
import hashlib
import json
import requests
import logging

__all__=["_search","newsearch","_requests","_sign"]

def _search(result, tag, subtag=None):
    tagvalue = None
    if result is None:
        pass
    else:
        rtext = result.text
        httpcode = result.status_code
        hetcode = result.json().get("code")
        if httpcode == 200:
            if hetcode == 0:
                if subtag:
                    data = result.json().get("data").get(tag)
                    tagvalue = [each.get(subtag) for each in data]
                else:
                    tagvalue = json.loads(rtext).get("data").get(tag)
            else:
                print('dsafdas')
                pass
        else:
            # mylogger.error(u"http请求失败:{code}".format(code=httpcode))
            pass
    return tagvalue

def _newsearch(result, tag):
    tagvalue = None
    data = None
    if result is None:
        pass
    else:
        rtext = result.text
        httpcode = result.status_code
        hetcode = result.json().get("code")
        if httpcode == 200:
            if hetcode == 0:
                datas = result.json().get("data")
                data = datas[0][tag]
            else:
                # mylogger.error(u"het请求失败：{text}".format(text=rtext))
                pass
        else:
            # mylogger.error(u"http请求失败:{code}".format(code=httpcode))
            pass
    return data


def _requests(url, arg, header, cookies=None):
    result = None
    try:
        if cookies:
            result = requests.post(url, data=arg, headers = header, cookies = cookies, verify = False)
        else:
            result = requests.post(url, data=arg, headers = header, verify = False)
        print(url)
        print(arg)
        print(result.json())
    except requests.exceptions.ConnectionError:
        # mylogger.error(u"链接失败")
        pass
    except requests.exceptions.SSLError:
        # mylogger.error(u"SSL错误")
        pass
    except requests.exceptions.HTTPError:
        # mylogger.error(u"HTTP错误")
        pass
    except requests.exceptions.Timeout:
        # mylogger.error(u"链接超时")
        pass
    return result

def _sign(method, url, appsecret, **arg):
    """将参数拼接后MD5得到签名"""
    return MD5("{}{}{}{}".format(method, url, _join(arg), appsecret))
    # return MD5("{}{}{}{}".format(method, url, arg, appsecret))

def _join(arg):
    """将参数拼接到一起"""
    sortarg = sorted(arg.iteritems(),key = lambda d: d[0])
    string = "&".join("{}={}".format(key,value) for key,value in sortarg)
    return string + "&"

def _myMD5(password, appsecret, pwdmd5):
    """对登录密码MD5"""
    return MD5(password+appsecret) if pwdmd5 else MD5(base64.b64encode(binascii.a2b_hex(MD5(password))) + appsecret)

def MD5(str):
    str = str.encode('utf-8')
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()
