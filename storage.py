# DB儲存資料
import pymssql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, DateTime, Boolean, Table, MetaData, DECIMAL, Date, NVARCHAR 
from sqlalchemy import insert
from utils.setting import mssqldb
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
    conn = pymssql.connect(db_settings)
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
    column_len = len(data[0].keys())
    while data:
        values, data = data[:2100//column_len], data[2100//column_len:]
        Momo_sale_db.insert(values=values, engine=mssqldb.engine)
    return

def pc_stock(data):
    '''
    pc 庫存
    '''
    column_len = len(data[0].keys())
    while data:
        values, data = data[:2100//column_len], data[2100//column_len]
        Pc_stock_db.insert(values=values, engine=mssqldb.engine)

class ModelMixin:
    @classmethod
    def insert(cls, values, engine):
        stmt = insert(cls)
        for value in values:
            stmt = stmt.values(**value)

        with sessionmaker(bind=engine)() as session:
            session.execute(stmt)
            session.commit()

# momo_sale_db回傳資料表格式
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

# pc_stock回傳資料表格式
class Pc_stock_db(Base, ModelMixin):
    __table_args__ = {"schema": "tableau"}
    __tablename__ = 'pc_stock'
    ps_id = Column(Integer, primary_key=True) #pk  (免帶)
    stock_datetime = Column(DateTime) #即時庫存抓取時間
    VendorPId = Column(NVARCHAR) #廠商料號(QC)
    ProdId = Column(NVARCHAR) #商品ID
    ProdName = Column(NVARCHAR) #商品名稱
    available_qty = Column(Integer) #可賣量
    #ins_date = Column(DateTime) #資料匯入時間 (免帶)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
