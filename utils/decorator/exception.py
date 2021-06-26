import traceback

from utils.common import logger
from utils.http import responser


# 捕获异常输出到日志
def exception_capture(fun):
    def wrapper(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except Exception as e:
            traceback.print_exc()
            logger.set_log(traceback.format_exc(), level='error')
            return responser.send(51000)

    return wrapper