# @Author :  Dylan  * 
# @Date :  2021-06-27 20:51:12  *
# @Last Modified by :    Dylan  * 
# @Last Modified time :  2021-06-27 20:51:12 

from __init__ import db
import json


# 定义好一些属性，与user表中的字段进行映射，并且这个属性要属于某个类型
class Sys_user(db.Model):
    __tablename__ = 'sys_user'

    uuid = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)  # id 整型，主键，自增，唯一
    username = db.Column(db.String(50),comment='账号')
    nickname = db.Column(db.String(50),comment='昵称')
    salt = db.Column(db.String(16),comment='密码盐')
    password=db.Column(db.String(32),comment='入库密码')
    role=db.Column(db.String(32),comment='角色')
    del_flag= db.Column(db.Integer,comment='')
    created_time=db.Column(db.Integer,comment='')
    updated_time=db.Column(db.Integer,comment='')
    created_user = db.Column(db.String(50),comment='')




