#coding=utf-8
from generator._read import *

class TestSplitURL:
    def test_split_url_null(self):
        assert split_URL("") == ("","","",{})

    def test_split_URL_string1(self):
        url = ("https://200.200.200.50/v1/app/csleep/tool/getMusicTools?"
            "accessToken=65b0b6e0c1fc415c8c43e0377216c9df&appId=10014&relateDeviceIds=&timestamp=1495867275515")
        assert split_URL(url) == ("https","200.200.200.50","v1/app/csleep/tool/getMusicTools",{
                "accessToken":"65b0b6e0c1fc415c8c43e0377216c9df",
                "appId":"10014",
                "relateDeviceIds":"",
                "timestamp":"1495867275515"})

    def test_split_url_string2(self):
        url = ("https200.200.200.50/v1/app/csleep/tool/getMusicTools?"
            "accessToken=65b0b6e0c1fc415c8c43e0377216c9df&appId=10014&relateDeviceIds=&timestamp=1495867275515")
        assert split_URL(url) == ("","","",{})

    def test_split_url_string3(self):
        url = ("https://200.200.200.50/v1/app/csleep/tool/getMusicTools")
        assert split_URL(url) == ("https","200.200.200.50","v1/app/csleep/tool/getMusicTools",{})

    def test_split_url_string4(self):
        url = ("https://")
        assert split_URL(url) == ("https","","",{})

    def test_split_url_string5(self):
        url = ("https://200.200.200.50//v1/app/csleep/tool/getMusicTools")
        assert split_URL(url) == ("https","200.200.200.50","v1/app/csleep/tool/getMusicTools",{})

class TestGetBoundary:
    def test_get_boundary_null(self):
        assert get_boundary({}) == None

    def test_get_boundary_dic1(self):
        header = {"a":"1","b":"2","c":"3"}
        assert get_boundary(header) == None

    def test_get_boundary_dic2(self):
        header = {"a":"1","b":"2","Content-Type":"multipart/form-data; boundary=Boundary+8978BA0B8BFDA159"}
        assert get_boundary(header) == "--Boundary+8978BA0B8BFDA159"

class TestGetPic:
    def test_get_pic_null(self):
        pass

    def test_get_pic_no(self):
        pass

    def test_get_pic_yes(self):
        pass

class TestReadHeader:
    def test_read_header_null(self):
        pass

    def test_read_header(self):
        pass

class TestReadReq:
    def test_read_req_null(self):
        pass

    def test_read_req(self):
        pass