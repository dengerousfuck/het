URLS = {
    "v1/account/login": [
        "accessToken",
        "refreshToken"
    ],
    "v1/user/room/list": [
        "roomId"
    ]
}

PARAMS = {
    "accessToken": r'"accessToken":"\w*"',
    "refreshToken": r'"refreshToken":"\w*"',
    "roomId": r'"roomId":\d*'
}

DATAS = {}