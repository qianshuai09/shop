# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request


route_user = Blueprint( 'user_page',__name__ )

@route_user.route( "/login",methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template( "user/login.html" )
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''


@route_user.route( "/edit" )
def edit():
    return render_template( "user/edit.html" )

@route_user.route( "/reset-pwd" )
def resetPwd():
    return render_template( "user/reset_pwd.html" )