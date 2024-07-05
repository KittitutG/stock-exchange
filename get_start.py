import yfinance as yf
from pprint import pprint
import pandas as pd

file_extension = '.xlsx'
file_name = 'result' + file_extension

bdms = yf.Ticker("BDMS.BK")

del bdms.info['companyOfficers']


df = pd.DataFrame(bdms.info,index=[0])

# with pd.ExcelWriter(file_name, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
#     df.to_excel(writer, 'Logs', index=False)


pprint(df)