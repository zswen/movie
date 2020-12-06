# -*- coding: utf-8 -*-
from flask import Blueprint,request,redirect
from application import app,db
from common.libs.Helper import ops_render,iPagenation
from common.libs.UrlManager import UrlManager
from sqlalchemy.sql.expression import func


index_page = Blueprint( "index_page",__name__ )

@index_page.route("/")
def index():
    return ops_render( "index.html", { "data": [],"pages":pages })

