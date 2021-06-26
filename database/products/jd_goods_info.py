# -*- coding: utf-8 -*-  
# @ Author: Dylan Leeee  
# @Date : 2021-06-26 13:11:53  
# @Last Modified by:   Dylan Leeee  
# @Last Modified time: 2021-06-26 13:11:53 

from __init__ import db
import datetime

# 定义好一些属性，与user表中的字段进行映射，并且这个属性要属于某个类型
class Jd_goods_info(db.Model):
    __tablename__ = 'jd_goods_info'

    uuid = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)  # id 整型，主键，自增，唯一
    code = db.Column(db.String(50),comment='商品编码')
    name = db.Column(db.String(256),comment='商品名称')
    skuid = db.Column(db.String(50),comment='商品id')
    is_jd_sale = db.Column(db.String(16),comment='是否京东自营')
    img_url = db.Column(db.String(256),comment='图片链接')
    best_price= db.Column(db.String(32),comment='活动价格')
    unit_price = db.Column(db.String(32),comment='京东单价')
    catagory = db.Column(db.String(50),comment='商品类别')
    material_url = db.Column(db.String(256),comment='商品链接')
    start_date = db.Column(db.DateTime, comment='活动开始时间')
    end_date = db.Column(db.DateTime, comment='活动结束时间')
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)