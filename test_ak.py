"""
    测试 akshare
"""
import akshare as ak #
stock_us_hist_df = ak.stock_us_daily(symbol='SPY', adjust='qfq').loc['2007-01-04':'2022-07-30',] 
print(stock_us_hist_df)



# from pandas_datareader import data as pdr
# data = pdr.get_data_yahoo()

import yfinance as yf #

stock_yf = yf.Ticker('SPY')
stock_us_hist_df = stock_yf.history(interval='1d', back_adjust=True, period='max',
                                            start='2007-01-04', end='2022-07-30',
                                            proxy='http://172.24.48.1:7890', )




print(stock_us_hist_df, stock_yf.info)


"""
amount	成交金额	精度：小数点后4位；单位：人民币元
adjustflag	复权状态	不复权、前复权、后复权
turn	换手率	精度：小数点后6位；单位：%
tradestatus	交易状态	1：正常交易 0：停牌
pctChg	涨跌幅（百分比）	精度：小数点后6位
peTTM	滚动市盈率	精度：小数点后6位
psTTM	滚动市销率	精度：小数点后6位
pcfNcfTTM	滚动市现率	精度：小数点后6位
pbMRQ	市净率	精度：小数点后6位
    
    """