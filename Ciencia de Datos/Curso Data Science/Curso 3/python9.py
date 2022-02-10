Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import pandas as pd
>>> import ssl
>>> ssl.SSLContext.verify_mode = ssl.VerifyMode.CERT_OPTIONAL
>>> df_can = pd.read_excel('https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2
                      )
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
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    df_can = pd.read_excel('https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx',
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/util/_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 457, in read_excel
    io = ExcelFile(io, storage_options=storage_options, engine=engine)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 1376, in __init__
    ext = inspect_excel_format(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 1250, in inspect_excel_format
    with get_handle(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/common.py", line 670, in get_handle
    ioargs = _get_filepath_or_buffer(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/common.py", line 339, in _get_filepath_or_buffer
    with urlopen(req_info) as req:
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
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)>
>>> df_can = pd.read_excel('https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2
                      )
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    df_can = pd.read_excel('https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx',
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/util/_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 457, in read_excel
    io = ExcelFile(io, storage_options=storage_options, engine=engine)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 1380, in __init__
    raise ValueError(
ValueError: Excel file format cannot be determined, you must specify an engine manually.
>>> df_can = pd.read_excel('https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2,
		       engine= 'openpyx1'
                      )
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    df_can = pd.read_excel('https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx',
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/util/_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 457, in read_excel
    io = ExcelFile(io, storage_options=storage_options, engine=engine)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 1351, in __init__
    raise ValueError(f"Unknown engine: {engine}")
ValueError: Unknown engine: openpyx1
>>> df_can = pd.read_excel('https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2,
		       engine= 'openpyxl'
                      )
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/compat/_optional.py", line 126, in import_optional_dependency
    module = importlib.import_module(name)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1030, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 984, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'openpyxl'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    df_can = pd.read_excel('https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx',
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/util/_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 457, in read_excel
    io = ExcelFile(io, storage_options=storage_options, engine=engine)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 1419, in __init__
    self._reader = self._engines[engine](self._io, storage_options=storage_options)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_openpyxl.py", line 524, in __init__
    import_optional_dependency("openpyxl")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/compat/_optional.py", line 129, in import_optional_dependency
    raise ImportError(msg)
ImportError: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.
>>> df_can = pd.read_excel('https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2,
		       engine= 'openpyxl'
                      )
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    df_can = pd.read_excel('https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx',
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/util/_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 457, in read_excel
    io = ExcelFile(io, storage_options=storage_options, engine=engine)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 1419, in __init__
    self._reader = self._engines[engine](self._io, storage_options=storage_options)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_openpyxl.py", line 525, in __init__
    super().__init__(filepath_or_buffer, storage_options=storage_options)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 518, in __init__
    self.book = self.load_workbook(self.handles.handle)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_openpyxl.py", line 536, in load_workbook
    return load_workbook(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/openpyxl/reader/excel.py", line 315, in load_workbook
    reader = ExcelReader(filename, read_only, keep_vba,
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/openpyxl/reader/excel.py", line 124, in __init__
    self.archive = _validate_archive(fn)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/openpyxl/reader/excel.py", line 96, in _validate_archive
    archive = ZipFile(filename, 'r')
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/zipfile.py", line 1257, in __init__
    self._RealGetContents()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/zipfile.py", line 1324, in _RealGetContents
    raise BadZipFile("File is not a zip file")
zipfile.BadZipFile: File is not a zip file
>>> print(df_can.shape)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(df_can.shape)
NameError: name 'df_can' is not defined
>>> df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
NameError: name 'df_can' is not defined
>>> df_can = pd.read_excel('/kaggle/input/immigration-to-canada-ibm-dataset/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print ('Data read into a pandas dataframe!')
SyntaxError: multiple statements found while compiling a single statement
>>> df_can = pd.read_excel('/kaggle/input/immigration-to-canada-ibm-dataset/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    df_can = pd.read_excel('/kaggle/input/immigration-to-canada-ibm-dataset/Canada.xlsx',
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/util/_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 457, in read_excel
    io = ExcelFile(io, storage_options=storage_options, engine=engine)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 1376, in __init__
    ext = inspect_excel_format(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 1250, in inspect_excel_format
    with get_handle(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/common.py", line 798, in get_handle
    handle = open(handle, ioargs.mode)
FileNotFoundError: [Errno 2] No such file or directory: '/kaggle/input/immigration-to-canada-ibm-dataset/Canada.xlsx'
>>> import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
SyntaxError: multiple statements found while compiling a single statement
>>> import os
>>> for dirname, _, filenames in os.walk('/kaggle/input'):
	for filename in filenames:
		print(os.path.join(dirname, filename))

	
>>> df_can = pd.read_excel('/kaggle/input/immigration-to-canada-ibm-dataset/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    df_can = pd.read_excel('/kaggle/input/immigration-to-canada-ibm-dataset/Canada.xlsx',
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/util/_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 457, in read_excel
    io = ExcelFile(io, storage_options=storage_options, engine=engine)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 1376, in __init__
    ext = inspect_excel_format(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/excel/_base.py", line 1250, in inspect_excel_format
    with get_handle(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/common.py", line 798, in get_handle
    handle = open(handle, ioargs.mode)
FileNotFoundError: [Errno 2] No such file or directory: '/kaggle/input/immigration-to-canada-ibm-dataset/Canada.xlsx'
>>> 
>>> 
>>> 
>>> #Ejercicio 2
>>> import matplotlib.pylot as plt
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    import matplotlib.pylot as plt
ModuleNotFoundError: No module named 'matplotlib.pylot'
>>> import matplotlib.pyplot as plt
>>> df= pd.read_csv("D:\\Python\\Articles\\matplotlib\\sales_data.csv")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    df= pd.read_csv("D:\\Python\\Articles\\matplotlib\\sales_data.csv")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/util/_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 680, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 575, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 933, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/parsers/readers.py", line 1217, in _make_engine
    self.handles = get_handle(  # type: ignore[call-overload]
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/io/common.py", line 789, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'D:\\Python\\Articles\\matplotlib\\sales_data.csv'
>>> df= pd.DataFrame