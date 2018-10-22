# -*- coding:utf-8 -*-
from web.controllers.api import route_api
from flask import request,jsonify,make_response
import json
@route_api.route("/food/food",methods=["GET","POST"])
def food():
    resp = {"code": 200, "msg": "GET Request Success", "data": {}}
    if request.method == "GET":
        return jsonify(resp)
    if request.method == "POST":
        req = request.values
        login_name = req['login_name'] if 'login_name' in req else ''
        login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
        if login_name is None or len(login_name) < 1:
            resp['code'] = -1
            resp['msg'] = '请输入正确的登录用户名~~'
            return jsonify(resp)
        if login_pwd is None or len(login_pwd) < 1:
            resp['code'] = -1
            resp['msg'] = '请输入正确的密码~~'
            return jsonify(resp)
        if login_name=='admin' and login_pwd=="admin":
            resp['code'] = 200
            resp['msg'] = '登陆成功'
            response = make_response(json.dumps( resp ))
            response.set_cookie('cookie',"dfgagatraea")
            return jsonify(resp)
        else:
            resp['code'] = 202
            resp['msg'] = '登陆失败'
            return jsonify(resp)

