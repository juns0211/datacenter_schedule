# 排程年月
import datetime

def example(params):
    '''
        params = {'supplierId':017217}   
    '''
    # dict 合併用法
    return {
        **params,
        'year': datetime.datetime.now().year,
        'month': datetime.datetime.now().month,
    }

def momo_sale(params):
    '''
        momo 銷售
    '''
    # 抓前一天資料
    return {
        **params,
        'reportDate': (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(f"%Y-%m-%d")
    }

def pchome_stock(params):
    '''
        pchome 庫存
    '''
    return params
