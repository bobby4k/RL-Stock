# import baostock as bs
import akshare as ak #
import pandas as pd #
import os #


OUTPUT = './stockdata'


def mkdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


class Downloader(object):
    def __init__(self,
                 output_dir,
                 date_start='1990-01-01',
                 date_end='2020-03-23'):
        self.date_start = date_start
        # self.date_end = datetime.datetime.now().strftime("%Y-%m-%d")
        self.date_end = date_end
        self.output_dir = output_dir
        self.fields = "date,code,open,high,low,close,volume" 
        # self.fields = "date,code,open,high,low,close,volume,amount," \
        #               "adjustflag,turn,tradestatus,pctChg,peTTM," \
        #               "pbMRQ,psTTM,pcfNcfTTM,isST"

    # def get_codes_by_date(self, date):
    #     print(date)
    #     stock_rs = bs.query_all_stock(date)
    #     stock_df = stock_rs.get_data()
    #     print(stock_df)
    #     return stock_df

    def run(self, symbol=[]):
        symbol = symbol if type(symbol).__name__ == 'list' else [symbol]
        
        for code in symbol:
            print("processing {}".format(code))
            df_code = ak.stock_us_daily(symbol=code, adjust='qfq').loc[self.date_start:self.date_end,] 

            df_code.to_csv(f'{self.output_dir}/{code}.{code}.csv', index=True)


if __name__ == '__main__':
    symbol = 'SPY'  #仅仅测试下spy
    
    # 获取股票的日K线数据
    mkdir('./stockdata/train')
    downloader = Downloader('./stockdata/train', date_start='2007-01-04', date_end='2020-01-07')
    downloader.run(symbol=symbol)

    mkdir('./stockdata/test')
    downloader = Downloader('./stockdata/test', date_start='2020-01-07', date_end='2022-07-29')
    downloader.run(symbol=symbol)

