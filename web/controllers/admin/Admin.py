# -*- coding:utf-8 -*-
from flask import Blueprint,redirect

route_admin = Blueprint( 'admin_page',__name__ )

@route_admin.route( "/index" )
def index():
    return redirect( "/src/views/index.html")