# -*- coding: utf-8 -*-
SERVER_PORT = 8999
DEBUG = False
SQLALCHEMY_ECHO = False
AUTH_COOKIE_NAME = "mooc_food"

##过滤url
IGNORE_URLS = [
    "^/user/login",
    "^/api",
    "^/admin"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

MINA_APP = {
    'appid':'wx0544aa8c403436ef',
    'appkey':'27652bed40d5822a372a54b126862d27'
}