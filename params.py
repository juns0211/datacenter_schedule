# 排程年月
import datetime

def example(params):
    '''
        params = {'supplierId':017217}   
    '''
    # dict 合併用法
    return params | {'year':datetime.datetime.now().year, 'month':datetime.datetime.now().month}
    