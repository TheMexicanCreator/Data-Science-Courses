Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from bs4 import BeautifulSoup
>>> import requests
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
>>> import requests
>>> html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
>>> soup= BeautifulSoup(html, "html.parser")
>>> print(soup.prettify())
<!DOCTYPE html>
<html>
 <head>
  <title>
   Page Title
  </title>
 </head>
 <body>
  <h3>
   <b id="boldest">
    Lebron James
   </b>
  </h3>
  <p>
   Salary: $ 92,000,000
  </p>
  <h3>
   Stephen Curry
  </h3>
  <p>
   Salary: $85,000, 000
  </p>
  <h3>
   Kevin Durant
  </h3>
  <p>
   Salary: $73,200, 000
  </p>
 </body>
</html>
>>> tag_object= soup.title
>>> print("tag object type:", type(tag_object))
tag object type: <class 'bs4.element.Tag'>
>>> tag_object= soup.h3
>>> print(tag_object)
<h3><b id="boldest">Lebron James</b></h3>
>>> tag_child= tag_object.b
>>> print(tag_child)
<b id="boldest">Lebron James</b>
>>> print(tag_object.parent)
<body><h3><b id="boldest">Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body>
>>> sibling_1= tag_object.next_sibling
>>> print(sibling_1)
<p> Salary: $ 92,000,000 </p>
>>> sibling_2= sibling_1.next_sibling
>>> print(sibling_2)
<h3> Stephen Curry</h3>
>>> sibling_3= sibling_2.next_sibling
>>> print(sibling_3)
<p> Salary: $85,000, 000 </p>
>>> 
>>> #Ejercicio 2
>>> table= "<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
>>> table_bs= BeautifulSoup(table, "html.parser")
>>> print(table.prettify())
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(table.prettify())
AttributeError: 'str' object has no attribute 'prettify'
>>> table_rows= table_bs.find_all('tr')
>>> print(table_rows)
[<tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>, <tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td><td>300 kg</td></tr>, <tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr>, <tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td><td>80 kg</td></tr>]
>>> first_row= table_rows[0]
>>> print(first_row)
<tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>
>>> print(type(first_row))
<class 'bs4.element.Tag'>
>>> print(first_row.td)
<td id="flight">Flight No</td>
>>> for i,row in enumerate(table_rows):
	print("row",i)
	cells=row.find_all('td')
	for j,cell in enumerate(cells):
		print('column',j,"cell",cell)

row 0
column 0 cell <td id="flight">Flight No</td>
column 1 cell <td>Launch site</td>
column 2 cell <td>Payload mass</td>
row 1
column 0 cell <td>1</td>
column 1 cell <td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td>
column 2 cell <td>300 kg</td>
row 2
column 0 cell <td>2</td>
column 1 cell <td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td>
column 2 cell <td>94 kg</td>
row 3
column 0 cell <td>3</td>
column 1 cell <td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td>
column 2 cell <td>80 kg</td>
>>> list_input= table_bs.find_all(name= ["tr","td"])
>>> print(list_input)
[<tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>, <td id="flight">Flight No</td>, <td>Launch site</td>, <td>Payload mass</td>, <tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td><td>300 kg</td></tr>, <td>1</td>, <td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td>, <td>300 kg</td>, <tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr>, <td>2</td>, <td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td>, <td>94 kg</td>, <tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td><td>80 kg</td></tr>, <td>3</td>, <td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td>, <td>80 kg</td>]
>>> print(table_bs.find_all(id= "flight"))
[<td id="flight">Flight No</td>]
>>> list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
>>> print(list_input)
[<a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a>, <a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a>]
>>> print(table_bs.find_all(href=True))
[<a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a>, <a href="https://en.wikipedia.org/wiki/Texas">Texas</a>, <a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a>]
>>> print(table_bs.find_all())
[<table><tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td><td>300 kg</td></tr><tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td><td>80 kg</td></tr></table>, <tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>, <td id="flight">Flight No</td>, <td>Launch site</td>, <td>Payload mass</td>, <tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td><td>300 kg</td></tr>, <td>1</td>, <td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td>, <a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a>, <a></a>, <td>300 kg</td>, <tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr>, <td>2</td>, <td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td>, <a href="https://en.wikipedia.org/wiki/Texas">Texas</a>, <td>94 kg</td>, <tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td><td>80 kg</td></tr>, <td>3</td>, <td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td>, <a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a>, <a> </a>, <td>80 kg</td>]
>>> print(table_bs.find_all(href=False))
[<table><tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td><td>300 kg</td></tr><tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td><td>80 kg</td></tr></table>, <tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>, <td id="flight">Flight No</td>, <td>Launch site</td>, <td>Payload mass</td>, <tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td><td>300 kg</td></tr>, <td>1</td>, <td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td>, <a></a>, <td>300 kg</td>, <tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr>, <td>2</td>, <td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td>, <td>94 kg</td>, <tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td><td>80 kg</td></tr>, <td>3</td>, <td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td>, <a> </a>, <td>80 kg</td>]
>>> print(soup.find_all(id= "boldest"))
[<b id="boldest">Lebron James</b>]
>>> #Ejercicio 3
>>> two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
>>> two_tables_bs= BeautifulSoup(two_tables, 'html.parser')
>>> print(two_tables_bs.find("table"))
<table class="rocket"><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table>
>>> print(two_tables_bs.find("table",class= 'pizza'))
SyntaxError: invalid syntax
>>> print(two_tables_bs.find("table",class_= 'pizza'))
<table class="pizza"><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td>144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr></table>
>>> #Ejercicio 4
>>> url= "http://www.ibm.com"
>>> data= requests.get(url).text
>>> soup= BeautifulSoup(data,"html.parser")
>>> for link in soup.find_all('a',href=True):
	print(link.get('href'))

https://www.ibm.com/mx/es
https://www.ibm.com/sitemap/mx/es
/mx-es/cloud/hybrid?lnk=hpv18l1
https://www.maratona.dev/es
/mx-es/cloud/cloud-pak-for-automation?lnk=hpv18f2
/mx-es/financing/pre-owned/ibm-certified-used-equipment?lnk=hpv18f2
/mx-es/products/openpages-with-watson?lnk=hpv18f3
/mx-es/cloud/cloud-pak-for-watson-aiops?lnk=hpv18f4
https://www.ibm.com/mx-es/products/?types%5B0%5D=trial
/mx-es/cloud/free?lnk=hpv18t1
/mx-es/products/cloud-pak-for-data?lnk=hpv18t2
/mx-es/products/spectrum-virtualize-for-public-cloud
/mx-es/cloud/watson-assistant?lnk=hpv18t3
/mx-es/security/identity-access-management/cloud-identity?lnk=hpv18t4
https://developer.ibm.com/es/depmodels/cloud/?lnk=hpv18ct16
https://developer.ibm.com/es/technologies/artificial-intelligence/?lnk=hpv18ct19
https://developer.ibm.com/es/?lnk=hpv18ct9
https://www.ibm.com/docs/es?lnk=hpv18ct14
https://www.redbooks.ibm.com/?lnk=ushpv18ct10
https://www.ibm.com/support/home/?lnk=hpv18ct11
https://www.ibm.com/training/?lnk=hpv18ct15
/mx-es/cloud
/cloud/hybrid?lnk=hpv18pt14
/mx-es/watson?lnk=ushpv18pt17
/mx-es/garage?lnk=hpv18pt13
/mx-es/blockchain?lnk=hpv18pt4
https://www.ibm.com/thought-leadership/institute-business-value/?lnk=hpv18pt12
/mx-es/analytics?lnk=hpv18pt1
/mx-es/security?lnk=hpv18pt9
/mx-es/financing?lnk=hpv18pt3
https://www.ibm.com/quantum-computing?lnk=hpv18pt16
/cloud/learn/public-cloud
/mx-es/cloud/learn/hybrid-cloud
/mx-es/cloud/satellite?lnk=hpv18ct1
/mx-es/cloud/redhat?lnk=hpv18ct13
/mx-es/watson?lnk=hpv18ct3
https://www.ibm.com/quantum-computing?lnk=hpv18ct18
/cloud/learn/kubernetes?lnk=hpv18ct8
/mx-es/products/spss-statistics?lnk=ushpv18ct7
/mx-es/blockchain?lnk=hpv18ct1
https://www.ibm.com/mx-es/employment?lnk=hpv18ct2
https://www.ibm.com/case-studies/coca-cola-european-partners/?lnk=hpv18cs1
/case-studies/search?lnk=hpv18cs2
#
>>> for link in soup.find_All('img')
SyntaxError: invalid syntax
>>> for link in soup.find_All('img'):
	print(link)
	print(link.get('src'))

Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    for link in soup.find_All('img'):
TypeError: 'NoneType' object is not callable
>>> for link in soup.find_all('img'):
	print(link)
	print(link.get('src'))

<img alt="Una computadora portátil en un escritorio que muestra un caso de uso para IBM Cloud Pak for Business Automation" class="" loading="lazy" src="//1.cms.s81c.com/sites/default/files/2021-02-17/cloud-pak-for-business-automation_0.jpg"/>
//1.cms.s81c.com/sites/default/files/2021-02-17/cloud-pak-for-business-automation_0.jpg
<img alt="" class="" loading="lazy" src="//1.cms.s81c.com/sites/default/files/2021-04-12/ICPO-Environmental-HP_1.jpg"/>
//1.cms.s81c.com/sites/default/files/2021-04-12/ICPO-Environmental-HP_1.jpg
<img alt="Una mujer utiliza OpenPages para comprobar la conformidad normativa" class="" loading="lazy" src="//1.cms.s81c.com/sites/default/files/2021-02-26/openpages-with-watson-444x254.jpg"/>
//1.cms.s81c.com/sites/default/files/2021-02-26/openpages-with-watson-444x254.jpg
<img alt="Ilustración isométrica con operaciones de IA" class="" loading="lazy" src="//1.cms.s81c.com/sites/default/files/2021-02-17/AIops-444x254.jpg"/>
//1.cms.s81c.com/sites/default/files/2021-02-17/AIops-444x254.jpg
<img alt="captura de pantalla del panel de control de IBM Cloud" class="" loading="lazy" src="//1.cms.s81c.com/sites/default/files/2021-02-17/ibm-cloud-trial.png"/>
//1.cms.s81c.com/sites/default/files/2021-02-17/ibm-cloud-trial.png
<img alt="Captura de pantalla de Cloud Pak for Data" class="" loading="lazy" src="//1.cms.s81c.com/sites/default/files/2021-02-17/cloud-pak-for-data-trial.png"/>
//1.cms.s81c.com/sites/default/files/2021-02-17/cloud-pak-for-data-trial.png
<img alt="" class="" loading="lazy" src="//1.cms.s81c.com/sites/default/files/2021-11-10/Storwize-V5000E-22330-700x420_4.png"/>
//1.cms.s81c.com/sites/default/files/2021-11-10/Storwize-V5000E-22330-700x420_4.png
<img alt="Captura de pantalla del software de Watson Assistant" class="" loading="lazy" src="//1.cms.s81c.com/sites/default/files/2021-02-17/watson-assistant-trial_0.png"/>
//1.cms.s81c.com/sites/default/files/2021-02-17/watson-assistant-trial_0.png
<img alt="captura de pantalla de software de seguridad" class="" loading="lazy" src="//1.cms.s81c.com/sites/default/files/2021-02-19/security-verify-trial.png"/>
//1.cms.s81c.com/sites/default/files/2021-02-19/security-verify-trial.png
>>> 
>>> #Ejercicio 5
>>> url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
>>> data= requests.get(url).text
>>> soup= BeautifulSoup(data,"html.parser")
>>> table= soup.find('table')
>>> for rwo in table.find_all('tr'):
	cols= row.find_all('td')
	color_name= cols[2].string
	color_code= cols[3].string
	print("{}--->{}".format(color_name,color_code))

Traceback (most recent call last):
  File "<pyshell#84>", line 4, in <module>
    color_code= cols[3].string
IndexError: list index out of range
>>> for row in table.find_all('tr'):
	cols= row.find_all('td')
	color_name= cols[2].string
	color_code= cols[3].string
	print("{}--->{}".format(color_name,color_code))

Color Name--->None
lightsalmon--->#FFA07A
salmon--->#FA8072
darksalmon--->#E9967A
lightcoral--->#F08080
coral--->#FF7F50
tomato--->#FF6347
orangered--->#FF4500
gold--->#FFD700
orange--->#FFA500
darkorange--->#FF8C00
lightyellow--->#FFFFE0
lemonchiffon--->#FFFACD
papayawhip--->#FFEFD5
moccasin--->#FFE4B5
peachpuff--->#FFDAB9
palegoldenrod--->#EEE8AA
khaki--->#F0E68C
darkkhaki--->#BDB76B
yellow--->#FFFF00
lawngreen--->#7CFC00
chartreuse--->#7FFF00
limegreen--->#32CD32
lime--->#00FF00
forestgreen--->#228B22
green--->#008000
powderblue--->#B0E0E6
lightblue--->#ADD8E6
lightskyblue--->#87CEFA
skyblue--->#87CEEB
deepskyblue--->#00BFFF
lightsteelblue--->#B0C4DE
dodgerblue--->#1E90FF
>>> 
>>> #Ejercicio 6
ç
>>> import pandas as pd
>>> url = "https://en.wikipedia.org/wiki/World_population"
>>> data= requests.get(url).text
>>> soup= BeautifulSoup(data,"html.parser")
>>> tables= soup.find_all('table')
>>> print(len(tables))
26
>>> for index,table in enumerate(tables):
	if ("10 most densely populated countries" in str(table):
	    
SyntaxError: invalid syntax
>>> for index,table in enumerate(tables):
	if ("10 most densely populated countries" in str(table)):
		table_index= index
print(table_index)
SyntaxError: invalid syntax
>>> for index,table in enumerate(tables):
	if ("10 most densely populated countries" in str(table)):
		table_index= index
	print(table_index)

Traceback (most recent call last):
  File "<pyshell#104>", line 4, in <module>
    print(table_index)
NameError: name 'table_index' is not defined
>>> for index,table in enumerate(tables):
	if ("10 most densely populated countries" in str(table)):
		table_index= indexprint(table_index)

		
Traceback (most recent call last):
  File "<pyshell#106>", line 3, in <module>
    table_index= indexprint(table_index)
NameError: name 'indexprint' is not defined
>>> for index,table in enumerate(tables):
	if ("10 most densely populated countries" in str(table)):
		table_index= index
		print(table_index)

5
>>> print(tables[table_index].prettify())
<table class="wikitable sortable" style="text-align:right">
 <caption>
  10 most densely populated countries
  <small>
   (with population above 5 million)
  </small>
 </caption>
 <tbody>
  <tr>
   <th>
    Rank
   </th>
   <th>
    Country
   </th>
   <th>
    Population
   </th>
   <th>
    Area
    <br/>
    <small>
     (km
     <sup>
      2
     </sup>
     )
    </small>
   </th>
   <th>
    Density
    <br/>
    <small>
     (pop/km
     <sup>
      2
     </sup>
     )
    </small>
   </th>
  </tr>
  <tr>
   <td>
    1
   </td>
   <td align="left">
    <span class="flagicon">
     <img alt="" class="thumbborder" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/23px-Flag_of_Singapore.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/35px-Flag_of_Singapore.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flag_of_Singapore.svg/45px-Flag_of_Singapore.svg.png 2x" width="23"/>
    </span>
    <a href="/wiki/Singapore" title="Singapore">
     Singapore
    </a>
   </td>
   <td>
    5,704,000
   </td>
   <td>
    710
   </td>
   <td>
    8,033
   </td>
  </tr>
  <tr>
   <td>
    2
   </td>
   <td align="left">
    <span class="flagicon">
     <img alt="" class="thumbborder" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Flag_of_Bangladesh.svg/23px-Flag_of_Bangladesh.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Flag_of_Bangladesh.svg/35px-Flag_of_Bangladesh.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Flag_of_Bangladesh.svg/46px-Flag_of_Bangladesh.svg.png 2x" width="23"/>
    </span>
    <a href="/wiki/Bangladesh" title="Bangladesh">
     Bangladesh
    </a>
   </td>
   <td>
    172,120,000
   </td>
   <td>
    143,998
   </td>
   <td>
    1,195
   </td>
  </tr>
  <tr>
   <td>
    3
   </td>
   <td align="left">
    <p>
     <span class="flagicon">
      <img alt="" class="thumbborder" data-file-height="600" data-file-width="1200" decoding="async" height="12" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/00/Flag_of_Palestine.svg/23px-Flag_of_Palestine.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/00/Flag_of_Palestine.svg/35px-Flag_of_Palestine.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/00/Flag_of_Palestine.svg/46px-Flag_of_Palestine.svg.png 2x" width="23"/>
     </span>
     <a href="/wiki/State_of_Palestine" title="State of Palestine">
      Palestine
     </a>
    </p>
   </td>
   <td>
    5,266,785
   </td>
   <td>
    6,020
   </td>
   <td>
    847
   </td>
  </tr>
  <tr>
   <td>
    4
   </td>
   <td align="left">
    <span class="flagicon">
     <img alt="" class="thumbborder" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/59/Flag_of_Lebanon.svg/23px-Flag_of_Lebanon.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/59/Flag_of_Lebanon.svg/35px-Flag_of_Lebanon.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/59/Flag_of_Lebanon.svg/45px-Flag_of_Lebanon.svg.png 2x" width="23"/>
    </span>
    <a href="/wiki/Lebanon" title="Lebanon">
     Lebanon
    </a>
   </td>
   <td>
    6,856,000
   </td>
   <td>
    10,452
   </td>
   <td>
    656
   </td>
  </tr>
  <tr>
   <td>
    5
   </td>
   <td align="left">
    <span class="flagicon">
     <img alt="" class="thumbborder" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/23px-Flag_of_the_Republic_of_China.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/35px-Flag_of_the_Republic_of_China.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/72/Flag_of_the_Republic_of_China.svg/45px-Flag_of_the_Republic_of_China.svg.png 2x" width="23"/>
    </span>
    <a href="/wiki/Taiwan" title="Taiwan">
     Taiwan
    </a>
   </td>
   <td>
    23,604,000
   </td>
   <td>
    36,193
   </td>
   <td>
    652
   </td>
  </tr>
  <tr>
   <td>
    6
   </td>
   <td align="left">
    <span class="flagicon">
     <img alt="" class="thumbborder" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/23px-Flag_of_South_Korea.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/35px-Flag_of_South_Korea.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_South_Korea.svg/45px-Flag_of_South_Korea.svg.png 2x" width="23"/>
    </span>
    <a href="/wiki/South_Korea" title="South Korea">
     South Korea
    </a>
   </td>
   <td>
    51,781,000
   </td>
   <td>
    99,538
   </td>
   <td>
    520
   </td>
  </tr>
  <tr>
   <td>
    7
   </td>
   <td align="left">
    <span class="flagicon">
     <img alt="" class="thumbborder" data-file-height="720" data-file-width="1080" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/17/Flag_of_Rwanda.svg/23px-Flag_of_Rwanda.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/17/Flag_of_Rwanda.svg/35px-Flag_of_Rwanda.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/17/Flag_of_Rwanda.svg/45px-Flag_of_Rwanda.svg.png 2x" width="23"/>
    </span>
    <a href="/wiki/Rwanda" title="Rwanda">
     Rwanda
    </a>
   </td>
   <td>
    12,374,000
   </td>
   <td>
    26,338
   </td>
   <td>
    470
   </td>
  </tr>
  <tr>
   <td>
    8
   </td>
   <td align="left">
    <span class="flagicon">
     <img alt="" class="thumbborder" data-file-height="600" data-file-width="1000" decoding="async" height="14" src="//upload.wikimedia.org/wikipedia/commons/thumb/5/56/Flag_of_Haiti.svg/23px-Flag_of_Haiti.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/5/56/Flag_of_Haiti.svg/35px-Flag_of_Haiti.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/5/56/Flag_of_Haiti.svg/46px-Flag_of_Haiti.svg.png 2x" width="23"/>
    </span>
    <a href="/wiki/Haiti" title="Haiti">
     Haiti
    </a>
   </td>
   <td>
    11,578,000
   </td>
   <td>
    27,065
   </td>
   <td>
    428
   </td>
  </tr>
  <tr>
   <td>
    9
   </td>
   <td align="left">
    <span class="flagicon">
     <img alt="" class="thumbborder" data-file-height="600" data-file-width="900" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/23px-Flag_of_the_Netherlands.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/35px-Flag_of_the_Netherlands.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/20/Flag_of_the_Netherlands.svg/45px-Flag_of_the_Netherlands.svg.png 2x" width="23"/>
    </span>
    <a href="/wiki/Netherlands" title="Netherlands">
     Netherlands
    </a>
   </td>
   <td>
    17,680,000
   </td>
   <td>
    41,526
   </td>
   <td>
    426
   </td>
  </tr>
  <tr>
   <td>
    10
   </td>
   <td align="left">
    <span class="flagicon">
     <img alt="" class="thumbborder" data-file-height="800" data-file-width="1100" decoding="async" height="15" src="//upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Flag_of_Israel.svg/21px-Flag_of_Israel.svg.png" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Flag_of_Israel.svg/32px-Flag_of_Israel.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Flag_of_Israel.svg/41px-Flag_of_Israel.svg.png 2x" width="21"/>
    </span>
    <a href="/wiki/Israel" title="Israel">
     Israel
    </a>
   </td>
   <td>
    9,470,000
   </td>
   <td>
    22,072
   </td>
   <td>
    429
   </td>
  </tr>
 </tbody>
</table>

>>> population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

print(population_data)
>>> print(population_data)
Empty DataFrame
Columns: [Rank, Country, Population, Area, Density]
Index: []
>>> population_data= pd.DataFrame(columns=["Rank","Country","Population","Area","Density"])
>>> for row in tables[table_index].tbody.find_all("tr"):
	col= row.find_all("td")
	if (col != []):
		rank= col[0].text
		country= col[1].text
		population= col[2].text.strip()
		area= col[3].text.strip()
		density= col[4].text.strip()
		population_data= population_data.append({"Rank":rank,"Country":country,"Population":population,"Area":area,"Density":density}, ignore_index=True)
		print(population_data)


Warning (from warnings module):
  File "<pyshell#126>", line 9
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
  Rank     Country Population Area Density
0    1   Singapore  5,704,000  710   8,033

Warning (from warnings module):
  File "<pyshell#126>", line 9
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
  Rank      Country   Population     Area Density
0    1    Singapore    5,704,000      710   8,033
1    2   Bangladesh  172,120,000  143,998   1,195

Warning (from warnings module):
  File "<pyshell#126>", line 9
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
  Rank           Country   Population     Area Density
0    1         Singapore    5,704,000      710   8,033
1    2        Bangladesh  172,120,000  143,998   1,195
2    3  \n Palestine\n\n    5,266,785    6,020     847

Warning (from warnings module):
  File "<pyshell#126>", line 9
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
  Rank           Country   Population     Area Density
0    1         Singapore    5,704,000      710   8,033
1    2        Bangladesh  172,120,000  143,998   1,195
2    3  \n Palestine\n\n    5,266,785    6,020     847
3    4           Lebanon    6,856,000   10,452     656

Warning (from warnings module):
  File "<pyshell#126>", line 9
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
  Rank           Country   Population     Area Density
0    1         Singapore    5,704,000      710   8,033
1    2        Bangladesh  172,120,000  143,998   1,195
2    3  \n Palestine\n\n    5,266,785    6,020     847
3    4           Lebanon    6,856,000   10,452     656
4    5            Taiwan   23,604,000   36,193     652

Warning (from warnings module):
  File "<pyshell#126>", line 9
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
  Rank           Country   Population     Area Density
0    1         Singapore    5,704,000      710   8,033
1    2        Bangladesh  172,120,000  143,998   1,195
2    3  \n Palestine\n\n    5,266,785    6,020     847
3    4           Lebanon    6,856,000   10,452     656
4    5            Taiwan   23,604,000   36,193     652
5    6       South Korea   51,781,000   99,538     520

Warning (from warnings module):
  File "<pyshell#126>", line 9
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
  Rank           Country   Population     Area Density
0    1         Singapore    5,704,000      710   8,033
1    2        Bangladesh  172,120,000  143,998   1,195
2    3  \n Palestine\n\n    5,266,785    6,020     847
3    4           Lebanon    6,856,000   10,452     656
4    5            Taiwan   23,604,000   36,193     652
5    6       South Korea   51,781,000   99,538     520
6    7            Rwanda   12,374,000   26,338     470

Warning (from warnings module):
  File "<pyshell#126>", line 9
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
  Rank           Country   Population     Area Density
0    1         Singapore    5,704,000      710   8,033
1    2        Bangladesh  172,120,000  143,998   1,195
2    3  \n Palestine\n\n    5,266,785    6,020     847
3    4           Lebanon    6,856,000   10,452     656
4    5            Taiwan   23,604,000   36,193     652
5    6       South Korea   51,781,000   99,538     520
6    7            Rwanda   12,374,000   26,338     470
7    8             Haiti   11,578,000   27,065     428

Warning (from warnings module):
  File "<pyshell#126>", line 9
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
  Rank           Country   Population     Area Density
0    1         Singapore    5,704,000      710   8,033
1    2        Bangladesh  172,120,000  143,998   1,195
2    3  \n Palestine\n\n    5,266,785    6,020     847
3    4           Lebanon    6,856,000   10,452     656
4    5            Taiwan   23,604,000   36,193     652
5    6       South Korea   51,781,000   99,538     520
6    7            Rwanda   12,374,000   26,338     470
7    8             Haiti   11,578,000   27,065     428
8    9       Netherlands   17,680,000   41,526     426

Warning (from warnings module):
  File "<pyshell#126>", line 9
FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
  Rank           Country   Population     Area Density
0    1         Singapore    5,704,000      710   8,033
1    2        Bangladesh  172,120,000  143,998   1,195
2    3  \n Palestine\n\n    5,266,785    6,020     847
3    4           Lebanon    6,856,000   10,452     656
4    5            Taiwan   23,604,000   36,193     652
5    6       South Korea   51,781,000   99,538     520
6    7            Rwanda   12,374,000   26,338     470
7    8             Haiti   11,578,000   27,065     428
8    9       Netherlands   17,680,000   41,526     426
9   10            Israel    9,470,000   22,072     429
>>> 