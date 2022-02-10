Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Ejercicio 1
>>> import nltk
>>> import os
>>> os.getcwd()
'/Users/robertogarcia/Documents'
>>> os.chdir('/Users/robertogarcia/Documents/Ciencia de Datos/Machine Learning')
>>> with open('brown_corpus_ca10.txt','r') as myfile:
	data= myfile.read().replace('\n', '')

	
>>> data2= data.replace("/", "")
>>> for i, line in enumerate(data2.split('\n')):
	if i > 10:
		break
	print(str(i) + ':\t' + line)


>>> from nltk import sent_tokenize, word_tokenize
>>> sent_tokenize(data2)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    sent_tokenize(data2)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/tokenize/__init__.py", line 106, in sent_tokenize
    tokenizer = load(f"tokenizers/punkt/{language}.pickle")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/data.py", line 750, in load
    opened_resource = _open(resource_url)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/data.py", line 876, in _open
    return find(path_, path + [""]).open()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mpunkt[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('punkt')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mtokenizers/punkt/PY3/english.pickle[0m

  Searched in:
    - '/Users/robertogarcia/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/share/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/lib/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
    - ''
**********************************************************************

>>> for sent in sent_tokenize(data2):
	print(word_tokenize)

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    for sent in sent_tokenize(data2):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/tokenize/__init__.py", line 106, in sent_tokenize
    tokenizer = load(f"tokenizers/punkt/{language}.pickle")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/data.py", line 750, in load
    opened_resource = _open(resource_url)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/data.py", line 876, in _open
    return find(path_, path + [""]).open()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mpunkt[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('punkt')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mtokenizers/punkt/PY3/english.pickle[0m

  Searched in:
    - '/Users/robertogarcia/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/share/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/lib/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
    - ''
**********************************************************************

>>> from nltk.corpus import stopwords
>>> stopwords_en= stopwords.words('english')
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/corpus/util.py", line 84, in __load
    root = nltk.data.find(f"{self.subdir}/{zip_name}")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mstopwords[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('stopwords')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/stopwords.zip/stopwords/[0m

  Searched in:
    - '/Users/robertogarcia/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/share/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/lib/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
**********************************************************************


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    stopwords_en= stopwords.words('english')
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/corpus/util.py", line 121, in __getattr__
    self.__load()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/corpus/util.py", line 86, in __load
    raise e
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/corpus/util.py", line 81, in __load
    root = nltk.data.find(f"{self.subdir}/{self.__name}")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/nltk/data.py", line 583, in find
    raise LookupError(resource_not_found)
LookupError: 
**********************************************************************
  Resource [93mstopwords[0m not found.
  Please use the NLTK Downloader to obtain the resource:

  [31m>>> import nltk
  >>> nltk.download('stopwords')
  [0m
  For more information see: https://www.nltk.org/data.html

  Attempted to load [93mcorpora/stopwords[0m

  Searched in:
    - '/Users/robertogarcia/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/share/nltk_data'
    - '/Library/Frameworks/Python.framework/Versions/3.9/lib/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
**********************************************************************

>>> nltk.download()
showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
True
>>> sent_tokenize(data2)

>>> stopwords_en= stopwords.words('english')
>>> print(stopwords_en)
['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
>>> 