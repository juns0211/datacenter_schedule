from pathlib import Path
import yaml
from decouple import config
from importlib import resources
BASE_PATH = Path(__file__).parent

# 讀取設定檔
with resources.open_binary('utils', 'config.yaml') as f:
    cf = yaml.load(f, Loader=yaml.Loader)
    MSSQL_DB_SETTING = cf['MSSQL_DB_SETTING']
    TEST_MSSQL_DB_SETTING = cf['TEST_MSSQL_DB_SETTING']

# 讀取設定檔
# with (BASE_PATH / 'config.yaml').open(encoding='utf8') as f:
#     cf = yaml.load(f, Loader=yaml.Loader)
#     MSSQL_DB_SETTING = cf['MSSQL_DB_SETTING']
#     TEST_MSSQL_DB_SETTING = cf['TEST_MSSQL_DB_SETTING']

# MSSQL
from .db import Database
if config('PY_ENV', 'prod') == 'prod':
    mssqldb = Database(MSSQL_DB_SETTING)
else:
    mssqldb = Database(TEST_MSSQL_DB_SETTING)