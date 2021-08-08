from __init__ import db
from utils.http import responser
from database.products.jd_goods_info import Jd_goods_info
import json
import datetime


def app_get_pruducts_info(catagory):
    rdata = []

    if not catagory: #   如果商品名为空，则查询所有
        goods_obj_list = Jd_goods_info.query.all()
    else:
        catagory = catagory.strip()
        goods_obj_list = Jd_goods_info.query.filter(Jd_goods_info.catagory.contains(catagory)).order_by(Jd_goods_info.created_at.asc()).all()

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


def app_get_pruducts_catagory():
    rdata = []
    filters = (
        db.cast(Jd_goods_info.end_date, db.DATE) >= db.cast(datetime.datetime.now(), db.DATE)
    )
    catagories = Jd_goods_info.query.with_entities(Jd_goods_info.catagory).all()
    n = 0
    same = []
    for cata in catagories:
        temp={}
        if cata.catagory in same:
            continue
        temp["id"] = n
        temp["name"] = cata.catagory
        same.append(cata.catagory)
        rdata.append(temp)
        n=n+1
    return responser.send(10000,rdata)
