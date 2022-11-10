# DB儲存資料
import pymysql

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
    db_settings = {
                        "host": "127.0.0.1",
                        "port": 3306,
                        "user": "root",
                        "password": "xxxxxxxxx",
                        "db": "xxxxx",
                        "charset": "utf8"
                    }
    conn = pymysql.connect(db_settings)
    with conn.cursor() as cursor:         
        command = "INSERT INTO charts(id, name, artist)VALUES(%s, %s, %s)"
        charts = charts.get_charts_tracks("H_PilcVhX-E8N0qr1-")
        for chart in charts:
            cursor.execute(
                command, (chart["id"], chart["name"], chart["album"]["artist"]["name"]))
        # 儲存變更
        conn.commit()
    return

