Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import requests
>>> from bs4 import BeautifulSoup
>>> url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
>>> data= requests.get(url).text
>>> soup= BeautifulSoup(data, 'html5lib')
>>> netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
>>> for row in soup.find("tbody").find_all('tr'):
	col= row.find_all("td")
	date= col[0].text
	Open= col[1].text
	high= col[2].text
	low= col[3].text
	close= col[4].text
	adj_close= col[5].text
	volume= col[6].text
	 netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)
	 
SyntaxError: unexpected indent
>>> for row in soup.find("tbody").find_all('tr'):
	col= row.find_all("td")
	date= col[0].text
	Open= col[1].text
	high= col[2].text
	low= col[3].text
	close= col[4].text
	adj_close= col[5].text
	volume= col[6].text
	netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)
	print(netflix_data.head())


Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close      Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21  78,560,600    528.21

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close      Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21  78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81  66,927,600    502.81

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85

Warning (from warnings module):
  File "<pyshell#28>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date    Open    High     Low   Close       Volume Adj Close
0  Jun 01, 2021  504.01  536.13  482.14  528.21   78,560,600    528.21
1  May 01, 2021  512.65  518.95  478.54  502.81   66,927,600    502.81
2  Apr 01, 2021  529.93  563.56  499.00  513.47  111,573,300    513.47
3  Mar 01, 2021  545.57  556.99  492.85  521.66   90,183,900    521.66
4  Feb 01, 2021  536.79  566.65  518.28  538.85   61,902,300    538.85
>>> read_html_pandas_data= pd.read_html(url)
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 1346, in do_open
    h.request(req.get_method(), req.selector, req.data, headers,
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 1285, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 1331, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 1280, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 1040, in _send_output
    self.send(msg)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 980, in send
    self.connect()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 1454, in connect
    self.sock = self._context.wrap_socket(self.sock,
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ssl.py", line 500, in wrap_socket
    return self.sslsocket_class._create(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ssl.py", line 1040, in _create
    self.do_handshake()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ssl.py", line 1309, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1129)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    read_html_pandas_data= pd.read_html(url)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/util/_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/html.py", line 1113, in read_html
    return _parse(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/html.py", line 919, in _parse
    tables = p.parse_tables()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/html.py", line 239, in parse_tables
    tables = self._parse_tables(self._build_doc(), self.match, self.attrs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/html.py", line 758, in _build_doc
    raise e
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/html.py", line 739, in _build_doc
    with urlopen(self.io) as f:
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/common.py", line 239, in urlopen
    return urllib.request.urlopen(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 214, in urlopen
    return opener.open(url, data, timeout)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 517, in open
    response = self._open(req, data)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 534, in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 494, in _call_chain
    result = func(*args)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 1389, in https_open
    return self.do_open(http.client.HTTPSConnection, req,
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 1349, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1129)>
>>> read_html_pandas_data= pd.read_html(str(soup))
>>> netflix_dataframe= read_html_pandas_data[0]
>>> print(netflix_dataframe.head())
           Date    Open    High     Low  Close* Adj Close**     Volume
0  Jun 01, 2021  504.01  536.13  482.14  528.21      528.21   78560600
1  May 01, 2021  512.65  518.95  478.54  502.81      502.81   66927600
2  Apr 01, 2021  529.93  563.56  499.00  513.47      513.47  111573300
3  Mar 01, 2021  545.57  556.99  492.85  521.66      521.66   90183900
4  Feb 01, 2021  536.79  566.65  518.28  538.85      538.85   61902300
>>> 
>>> 
>>> #Ejercicio 2
>>> url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
>>> data= requests.get(url).text
>>> soup= BeautifulSoup(data, 'html5lib')
>>> amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
>>> for row in soup.find("tbody").find_all("tr")_
SyntaxError: invalid syntax
>>> for row in soup.find("tbody").find_all("tr"):
	col= row.find_all("td")
	date= col[0].text
	Open= col[1].text
	high= col[2].text
	low= col[3].text
	close= col[4].text
	adj_close= col[5].text
	volume= col[6].text
	amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)
	print(amazon_data.head())


Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close      Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20  71,528,900  3,206.20

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close      Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20  71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93  77,556,200  3,256.93

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close      Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20  71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93  77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04  90,810,500  3,168.04

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73

Warning (from warnings module):
  File "<pyshell#52>", line 10
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
           Date      Open      High       Low     Close       Volume Adj Close
0  Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20   71,528,900  3,206.20
1  Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93   77,556,200  3,256.93
2  Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04   90,810,500  3,168.04
3  Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  116,226,100  3,036.15
4  Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  115,899,300  3,148.73
>>> read_html_pandas_data= pd.read_html(str(soup))
>>> amazon_dataframe= read_html_pandas_data[0]
>>> print(amazon_dataframe.head())
           Date     Open     High      Low   Close* Adj Close**     Volume
0  Jan 01, 2021  3270.00  3363.89  3086.00  3206.20     3206.20   71528900
1  Dec 01, 2020  3188.50  3350.65  3072.82  3256.93     3256.93   77556200
2  Nov 01, 2020  3061.74  3366.80  2950.12  3168.04     3168.04   90810500
3  Oct 01, 2020  3208.00  3496.24  3019.00  3036.15     3036.15  116226100
4  Sep 01, 2020  3489.58  3552.25  2871.00  3148.73     3148.73  115899300
>>> df1= df.head(5)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    df1= df.head(5)
NameError: name 'df' is not defined
>>> print(df1)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    print(df1)
NameError: name 'df1' is not defined
>>> df1= amazon_dataframe.head(5)
>>> print(df1)
           Date     Open     High      Low   Close* Adj Close**     Volume
0  Jan 01, 2021  3270.00  3363.89  3086.00  3206.20     3206.20   71528900
1  Dec 01, 2020  3188.50  3350.65  3072.82  3256.93     3256.93   77556200
2  Nov 01, 2020  3061.74  3366.80  2950.12  3168.04     3168.04   90810500
3  Oct 01, 2020  3208.00  3496.24  3019.00  3036.15     3036.15  116226100
4  Sep 01, 2020  3489.58  3552.25  2871.00  3148.73     3148.73  115899300
>>> df2= amazon_dataframe.head(3)
>>> print(df2)
           Date     Open     High      Low   Close* Adj Close**    Volume
0  Jan 01, 2021  3270.00  3363.89  3086.00  3206.20     3206.20  71528900
1  Dec 01, 2020  3188.50  3350.65  3072.82  3256.93     3256.93  77556200
2  Nov 01, 2020  3061.74  3366.80  2950.12  3168.04     3168.04  90810500
>>> 