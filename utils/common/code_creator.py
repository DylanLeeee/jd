import random
import string
import time


def get_code(key):
    # 统一为六位数，保持长度一致
    TAGS = {
        'jd_goods_info':'JDGOIN'
    }
    if TAGS.get(key):
        rd = ''.join(random.sample(string.ascii_letters + string.digits, 16))
        ts = str(int(time.time()))
        code = TAGS[key] + rd + ts
        return code
    else:
        return False