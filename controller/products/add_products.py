# -*- coding: utf-8 -*-  
# @ Author: Dylan Leeee  
# @Date : 2021-06-26 12:50:57  
# @Last Modified by:   Dylan Leeee  
# @Last Modified time: 2021-06-26 12:50:57 


from __init__ import app
from __init__ import request
import json
from utils.decorator.oauth2_tool import oauth2_check
from utils.jd.jd_client import JdApiClient
from utils.http import responser
# from service.admin import sys_user_manager
from service.products import add_products_manager


@app.route("/get_product_info",methods=["GET","POST"])
def get_product_info():
    res_status, rjson = responser.post_param_check(request, ['skuid', 'bestPrice'])
    if res_status == 'success':
        return add_products_manager.add_products_by_one( rjson['skuid'], rjson['bestPrice'])
    else:
        return rjson


@app.route("/get_goods_list",methods=["GET","POST"])
def get_goods_list():
    res_status, rjson = responser.post_param_check(request, ['goodsName'])
    if res_status == 'success':
        return add_products_manager.get_goods_list( rjson['goodsName'])
    else:
        return rjson