
import tushare as ts

pro = ts.pro_api('a460665afee70da5db824d696b636fa40e577db109de25960134f8e4')
#查询当前所有正常上市交易的股票列表
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
print(data)

