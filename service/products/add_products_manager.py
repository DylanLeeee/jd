# @Author: Dylan Leeee  
# @Date: 2021-06-26 12:44:46  
# @Last Modified by:   Dylan Leeee  
# @Last Modified time: 2021-06-26 12:44:46 
 

from __init__ import db
# from config import USER_SALT_LENGTH,PAGE_LIMIT, DEFAULT_PAGE
# from sqlalchemy import func,or_
# from database.sys_user import Sys_user
from utils.http import responser
from utils.jd import jd_client
# from utils.decorator import oauth2_tool
from config import JD_KEY, JD_SECRET
from utils.jd import jd_client
from database.products.jd_goods_info import Jd_goods_info
import json
from utils.common.code_creator import get_code
import datetime

client = jd_client.JdApiClient(JD_KEY, JD_SECRET)
# 通过商品id 新增商品
def add_products_by_one(jd_id, best_price):
    if not all([jd_id, best_price]):
        return responser.send(10005)
    param = {"skuIds":jd_id}
    resp = client.call("jd.union.open.goods.promotiongoodsinfo.query",
                    param)
    rdata = resp.json()['jd_union_open_goods_promotiongoodsinfo_query_response']['result']
    if rdata:
        rdata = json.loads(rdata)
        if rdata.get("code") == 200:
            for item in rdata.get("data"):
                code = get_code('jd_goods_info')
                unit_price = item.get('unitPrice')
                material_url = item.get('materialUrl')
                start_date = item.get('startDate')
                start_date = str(datetime.datetime.fromtimestamp(start_date/1000))
                end_date = item.get('endDate')
                end_date = str(datetime.datetime.fromtimestamp(end_date/1000))
                is_jd_sale = item.get('isJdSale')
                name = item.get('goodsName')
                skuid = item.get('skuId')
                img_url = item.get('imgUrl')
                catagory = item.get('cid3Name')
                jd_obj = Jd_goods_info(code=code, name=name, skuid=skuid,is_jd_sale=is_jd_sale,img_url=img_url,
                                        best_price=best_price, unit_price=unit_price, catagory=catagory,
                                        material_url=material_url,start_date=start_date, end_date=end_date)
                db.session.add(jd_obj)
                db.session.commit()
            return responser.send(10000)

    return responser.send(10004)


def get_goods_list(goods_name):
    rdata = []
    filters = (
        db.cast(Jd_goods_info.end_date, db.DATE) >= db.cast(datetime.datetime.now(), db.DATE)
    )

    if not goods_name: #   如果商品名为空，则查询所有
        goods_obj_list = Jd_goods_info.query.all()
    else:
        goods_name = goods_name.strip()
        goods_obj_list = Jd_goods_info.query.filter(*filters, Jd_goods_info.name.contains(goods_name)).all()

    for obj_item in  goods_obj_list:
        temp_dict = {}
        temp_dict['name'] = obj_item.name
        temp_dict['skuid'] = obj_item.skuid
        temp_dict['materialUrl'] = obj_item.material_url
        temp_dict['unitPrice'] = obj_item.unit_price
        temp_dict['bestPrice'] = obj_item.best_price
        temp_dict['imgUrl'] = obj_item.img_url
        temp_dict['startDate'] = str(obj_item.start_date.date())
        temp_dict['endDate'] = str(obj_item.end_date.date())
        temp_dict['catagory'] = obj_item.catagory
        temp_dict['isJdSale'] =obj_item.is_jd_sale
        rdata.append(temp_dict)
    return responser.send(10000,rdata)

        