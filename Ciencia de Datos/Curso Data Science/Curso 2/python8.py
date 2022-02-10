Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Ejercicio 1
>>> import yfinance as yf
>>> import pandas as pd
>>> import requests
>>> from bs4 import BeautifulSoup
>>> import plotly.graph_objects as go
>>> from plotly.subplots import make_subplots
>>> def make_graph(stock_data, revenue_data, stock):
	fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
	stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
	revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
	fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
	fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
	fig.update_xaxes(title_text="Date", row=1, col=1)
	fig.update_xaxes(title_text="Date", row=2, col=1)
	fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
	fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
	fig.update_layout(showlegend=False,
	height=900,
	title=stock,
	xaxis_rangeslider_visible=True)
	fig.show()

>>> tesla= yf.Ticker('TSLA')
>>> tesla_data= tesla.history(period= "max")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tesla_data= tesla.history(period= "max")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/yfinance/base.py", line 247, in history
    df.index = df.index.tz_localize("UTC").tz_convert(
AttributeError: 'Index' object has no attribute 'tz_localize'
>>> tesla_data.reset_index(inplace=True)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tesla_data.reset_index(inplace=True)
NameError: name 'tesla_data' is not defined
>>> print(tesla_data.head())
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(tesla_data.head())
NameError: name 'tesla_data' is not defined
>>> 
>>> #Ejercicio 2
>>> url= " https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
>>> data= requests.get(url).text
>>> soup= BeautifulSoup(data, "html.parser")
>>> print(soup.find_all('title'))
[<title>Tesla Revenue 2009-2021 | TSLA | MacroTrends</title>]
>>> tesla_revenue= pd.DataFrame(columns= ['Data', 'Revenue'])
>>> for row in soup.find_all("tbody")[1].find_all("tr"):
	col= row.find_all("td")
	date= col[0].text
	revenue= col[1].text.replace("$","").replace(",","")
	tesla_revenue= tesla_revenue.append({"Date":date, "Revenue":revenue}, ignore_index= True)


Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#39>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
>>> testa_revenue.dropna(inplace=True)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    testa_revenue.dropna(inplace=True)
NameError: name 'testa_revenue' is not defined
>>> tesla_revenue.dropna(inplace=True)
>>> tesla_revenue= tesla_revenue[tesla_revenue['Revenue'] != ""]
>>> print(tesla_revenue.tail())
Empty DataFrame
Columns: [Data, Revenue, Date]
Index: []
>>> #Ejercicio 3
>>> url= "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
>>> data= requests.get(url).text
>>> soup= BeautifulSoup(data, "html.parser")
>>> soup.find_all('title')
[<title>GameStop Revenue 2006-2021 | GME | MacroTrends</title>]
>>> gme_revenue= pd.DataFrame(columns= ['Data','Revenue'])
>>> for row in soup.find_all("tbody")[1].find_all("tr"):
	col= row.find_all("td")
	date= col[0].text
	revenue= col[1].text.replace("$","").replace(",","")
	gme_revenue= gme_revenue.append({"Date": date, "Revenue": revenue}, ignore_index = True)

	

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.

Warning (from warnings module):
  File "<pyshell#55>", line 5
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
>>> for row in soup.find_all("tbody")[1].find_all("tr"):
	col= row.find_all("td")
	date= col[0].text
	revenue= col[1].text.replace("$","").replace(",","")
	gme_revenue= gme_revenue.concat({"Date": date, "Revenue": revenue}, ignore_index = True)

Traceback (most recent call last):
  File "<pyshell#62>", line 5, in <module>
    gme_revenue= gme_revenue.concat({"Date": date, "Revenue": revenue}, ignore_index = True)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/generic.py", line 5583, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'concat'
>>> gme_revenue.dropna(inplace=True)
>>> gme_revenue= gme_revenue[gme_revenue['Revenue'] != ""]
>>> print(gme_revenue.tail())
Empty DataFrame
Columns: [Data, Revenue, Date]
Index: []
>>> make_graph(gme_data, gme_revenue, 'GameStop')
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    make_graph(gme_data, gme_revenue, 'GameStop')
NameError: name 'gme_data' is not defined
>>> 