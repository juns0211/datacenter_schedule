import datetime
# 資料清洗用fun

def example(data):
    '''
        data = {
                "order": [],
                "warehouse": [
                {
                    "品名": "【CorelleBrands 康寧餐具】微笑三色堇300ml馬克杯四入組",
                    "品號": "10009897",
                    "商品原廠編號": "1000041439",
                    "客退數量": "44",
                    "數量(訂購-取消)": "766",
                    "規格": "無",
                    "進價": "200",
                    "開發通路": "網路開發"
                },
                {
                    "品名": "【Schick 舒適牌】舒適5刮鬍刀 1刀把2刀片",
                    "品號": "10335743",
                    "商品原廠編號": "1000026607",
                    "客退數量": "4",
                    "數量(訂購-取消)": "1",
                    "規格": "無",
                    "進價": "160",
                    "開發通路": "網路開發"
                }],
                }
    '''
    order = data['order']
    warehouse = data['warehouse']
    wh_list = []
    for w in warehouse:
        wh_list.append({'品名':w['品名'],  '數量':int(w['客退數量']) + int(w['數量(訂購-取消)'])})

    # data參數回傳格式依照data傳進來時的原生格式
    return {'order':order, 'warehouse':wh_list}


def momo_sale(data):
    '''
    MOMO 銷售
    '''
    search_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    result = []
    for d in data:
        result.append(
                {
                        'order_day':search_date,
                        'available_qty': d['可接單量'],
                        'QC':  d['商品原廠編號'] if d['商品原廠編號'].isdigit() else None,
                        'product_name': d['商品名稱'],
                        'product_id': d['商品編號'],
                        'total_sale_qty': d['總販售量'],
                        'total_sale_price': d['訂購總金額'],
                        'product_sale_qty': d['訂購數量(訂購-取消)'],
                        'sale_qty': d['訂購數量(訂購-取消).1'],
                }
        )
    # data參數回傳格式依照data傳進來時的原生格式
    return result