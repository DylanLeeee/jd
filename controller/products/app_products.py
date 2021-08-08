from __init__ import app
from __init__ import request
import json
from utils.decorator.oauth2_tool import oauth2_check
from utils.jd.jd_client import JdApiClient
from utils.http import responser
# from service.admin import sys_user_manager
from service.products import app_products_manager


@app.route("/app_get_pruducts_info",methods=["GET","POST"])
def app_get_pruducts_info():
    res_status, rjson = responser.post_param_check(request, ['catagory'])
    if res_status == 'success':
        return app_products_manager.app_get_pruducts_info( rjson['catagory'])
    else:
        return rjson

@app.route("/app_get_pruducts_catagory",methods=["GET","POST"])
def app_get_pruducts_catagory():
    res_status, rjson = responser.post_param_check(request,[])
    if res_status == 'success':
        return app_products_manager.app_get_pruducts_catagory()
    else:
        return rjson


