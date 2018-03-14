
from apps.front.het_fiddler.util.script._myfunctools import *


class TestSplitParams:
    def test_split_params_null(self):
        assert split_params("") == {}

    def test_split_params_string(self):
        assert split_params("a=1&b=2&c=3&") == {"a": "1", "b": "2", "c": "3"}
        assert split_params("a=1&b=2&c=3") == {"a": "1", "b": "2", "c": "3"}


class TestDicToStr:
    def test_dic_to_str_null(self):
        assert dic_to_str({}) == ("", "")
        assert dic_to_str(None) == ("", "")

    def test_dic_to_str_dic(self):
        dic = {"a": "1", "b": "2", "c": "3"}
        assert dic_to_str(dic) == ("a|b|c", "1|2|3")


class TestStrToDic:
    def test_str_to_dic_null(self):
        assert str_to_dic("", "") == {}
        assert str_to_dic("", "1|2|3") == {}
        assert str_to_dic("a|b|c", "") == {}
        assert str_to_dic(None, None) == {}

    def test_str_to_dic_string(self):
        assert str_to_dic("a|b|c", "1|2|3") == {"a": "1", "b": "2", "c": "3"}
        assert str_to_dic("a|b|c", "||") == {"a": "", "b": "", "c": ""}
        assert str_to_dic("||", "||") == {"": ""}


class TestSearchUrl:
    def test_search_url_null(self):
        path = "V1/account/login"
        assert search_url("") == ""
        assert search_url(path) == ""

    def test_search_url_string(self):
        assert search_url("v1/account/login") == "accessToken|refreshToken"
        assert search_url("v1/user/room/list") == "roomId"


class TestSearchParams:
    def test_search_params_null(self):
        assert search_params({}) == ""

    def test_search_params_dic(self):
        dica = {"roomId": 1, "a": 2}
        dicb = {"roomId": 1, "accessToken": 2}
        assert search_params(dica) == "roomId"
        assert search_params(dicb) == "roomId|accessToken"
