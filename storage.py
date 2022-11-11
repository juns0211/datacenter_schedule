# DB儲存資料
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, DateTime, Boolean, Table, MetaData, DECIMAL, column, Date, NVARCHAR 
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, insert
from sqlalchemy import and_, or_
Base = declarative_base()

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


def momo_sale(data):
    '''
    momo 銷售
    '''
    db = {
            'url_port': '10.0.130.225',
            'acc': 'juns_chen',
            'pw': 'Juns1984',
            'db_name': 'DataTeam',
        }
    url_port = db['url_port']
    acc = db['acc']
    pw = db['pw']
    db_name = db['db_name']
    engine = create_engine(f'mssql://{acc}:{pw}@{url_port}/{db_name}?driver=SQL Server', connect_args={'timeout':600})
    Momo_sale_db.insert(values=data, engine=engine)
    return



class ModelMixin:
    @classmethod
    def insert(cls, values, engine):
        stmt = insert(cls, values=values)
        engine.execute(stmt)

# 回傳資料表格式
class Momo_sale_db(Base, ModelMixin):
    __table_args__ = {"schema": "tableau"}
    __tablename__ = 'momo_product_sale'
    mp_id = Column(Integer, primary_key=True) #pk  (免帶)
    order_day = Column(Date) #訂單日期
    available_qty = Column(Integer) #可接單量
    QC = Column(Integer) #商品原廠編號
    product_name = Column(NVARCHAR) #商品名稱
    product_id = Column(Integer) #商品編號
    total_sale_qty = Column(Integer) #總販售量
    total_sale_price = Column(DECIMAL) #訂購總金額
    product_sale_qty = Column(Integer) #訂購數量(訂購-取消)
    sale_qty = Column(Integer) #訂購數量(訂購-取消).1
    #ins_date = Column(DateTime) #資料匯入時間 (免帶)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
