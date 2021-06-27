# @Author :  Dylan  * 
# @Date :  2021-06-27 20:54:49  *
# @Last Modified by :    Dylan  * 
# @Last Modified time :  2021-06-27 20:54:49 


import requests
import json

def check_login(username,password):
    url = 'http://localhost:5000/login'
    rd = {
        'username':username,
        'password':password
    }
    rd=json.dumps(rd)
    res = requests.post(url,data=rd).text
    return res

'''
账号登录
'''
# res = check_login('admin','admin123')
