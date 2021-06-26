# @Author: Dylan Leeee  
# @Date: 2021-06-26 12:44:46  
# @Last Modified by:   Dylan Leeee  
# @Last Modified time: 2021-06-26 12:44:46 
 
import random
import string
import hashlib
from __init__ import db
from config import USER_SALT_LENGTH,PAGE_LIMIT, DEFAULT_PAGE
from sqlalchemy import func,or_
from database.sys_user import Sys_user
from utils.http import responser
from utils.jd import jd_client
from utils.decorator import oauth2_tool
from config import JD_KEY, JD_SECRET
from utils.jd import jd_client

client = jd_client.JdApiClient(JD_KEY, JD_SECRET)
# 通过商品id 新增商品
def add_products_by_one(skuid, best_price):
    param = {"skuIds":skuid}
    resp = client.call("jd.union.open.goods.promotiongoodsinfo.query",
                    param)
    rdata = resp.json()['jd_union_open_goods_promotiongoodsinfo_query_response']['result']
    
    
    return responser.send(10000,rdata)