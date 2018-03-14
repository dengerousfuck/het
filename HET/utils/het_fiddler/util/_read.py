import os
import sys
import logging
import binascii
import glob
import shutil
import time
import json

from urllib.parse import unquote
from functools import partial
from contextlib import contextmanager

# import _logger
from utils.het_fiddler.util.script._myfunctools import str_to_dic, dic_to_str, split_params, search_url, search_params, get_params, \
    update_params

# mylogger = _logger.Logger("read",logging.ERROR,logging.ERROR)
here = os.path.abspath(os.path.dirname(__file__))
get_path = partial(os.path.join, here)


def read(reqfiles, rspfiles, resultfile="result.sql"):
    with open(resultfile, mode="w", encoding="UTF-8") as rsf:
        reqs = read_req(reqfiles)
        rsps = read_rsp(rspfiles)
        for req, rsp in zip(reqs, rsps):
            # method, version, protocol, host, header, path, formkeys, formvalues, isurl, isparams = req
            casename, method, version, protocol, host, header, path, forms, isurl, isparams = req
            version, code, message, rspbody = rsp
            string = "                    ".join(
                (casename, method, version, protocol, host, path, forms, isurl, isparams, code, message, rspbody))
            rsf.write(string + "\n")
            # return method, version, protocol, host, header, path, formkeys, formvalues, isurl, isparams, code, message, rspbody


def read_rsp(files):
    for eachfile, dirname in files:
        with open(eachfile, mode="r", encoding="UTF-8") as f:
            firstline = f.readline().strip()
            version, code, message = firstline.split(" ")
            header = read_header(f)
            body = "".join(eachline.strip() for eachline in f)
            # mylogger.debug("\n{}\n{}\n{}\n{}".format(version, code, message, body))
        yield version, code, message, body


def read_req(files):
    """读取响应信息

    ：param files, type file：接口信息文件

    ：
    """
    for eachfile, dirname in files:
        with open(eachfile, mode="r", encoding="UTF-8") as f:
            firstline = f.readline().strip()
            method, url, version = firstline.split(" ")
            protocol, host, path, forms = split_URL(url)
            isurl = search_url(path.strip())
            header = read_header(f)
            if method.upper() == "POST":
                string = "".join(eachline for eachline in f).strip()
                boundary = get_boundary(header)
                forms = get_pic(string, boundary) if boundary else split_params(string)
            # formkeys,formvalues = dic_to_str(forms)
            isparams = search_params(forms)
            for key in forms.keys():
                if key in ["timestamp", "sign", "accessToken"]:
                    forms[key] = key + "_" + forms["appId"] if key == "accessToken" else key
            forms = json.dumps(forms)
        yield dirname[0], method, version, protocol, host, header, path, forms, isurl, isparams


def read_header(file):
    """读取请求头信息。读取到空行则立即结束

    :param file, type file：接口信息文件

    ：rsp header, type dic：请求头，字典类型
    """
    header = {}
    for eachline in file:
        string = eachline.strip()
        if not string:
            break
        key, value = string.split(":", 1)
        header[key] = value
    return header


def get_pic(string, splitword):
    """读取图片表单信息

    :param string:
    :param splitword:

    """
    forms = {}
    string = string[:-2]
    datas = [each.split("\r\n\r\n") for each in string.split(splitword) if each.strip()]
    path = {key.strip(): value.strip() for key, value in datas}
    for key, value in path.items():
        keystring = "".join(each for each in key.split(";") if " name=" in each)
        others, newkey = keystring.split(" name=")
        if newkey == '"avatar"':
            filename = "avatar-{}.txt".format(str(int(time.time() * 1000)))
            picpath = get_path("pic", filename)
            with open(picpath, "wb") as wf:
                wf.write(value)
            forms[newkey] = picpath
            continue
        forms[newkey] = (None, value)
    return forms


def get_boundary(header):
    """从请求头中获取图片分隔符boundary

    ：param header, type dic：请求头，字典类型

    ：rsp bounday, type str：图片分隔符
    """
    splitstring = "".join(value for key, value in header.items() if "boundary=" in value)
    if splitstring:
        others, boundary = "".join(each for each in splitstring.split(";") if "boundary=" in each).split("=")
        boundary = "".join(("--", boundary))
    else:
        boundary = None
    return boundary


def split_URL(url):
    """拆分url，返回协议、域名、路径、参数

    ：param url, type str：完整url

    ：rsp protocol, type str：协议，是http还是https
    ：rsp host, type str：域名
    ：rsp path, type str：路径
    ：rsp forms, type str：参数
    """
    string = unquote(url)
    protocol, others = string.split("://") if "//" in string else ("", "")
    others, param = others.split("?") if "?" in others else (others, "")
    host, path = others.split("/", 1) if others else ("", "")
    path = path[1:] if path.startswith("/") else path
    forms = split_params(param)
    return protocol, host, path, forms


