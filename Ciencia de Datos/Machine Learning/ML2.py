Python 3.9.10 (v3.9.10:f2f3f53782, Jan 13 2022, 17:02:14) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Ejercicio 1
>>> import pandas as pd
>>> import os
>>> os.getcwd()
'/Users/robertogarcia/Documents'
>>> os.chdir('/Users/robertogarcia/Documents/Ciencia de Datos/Machine Learning')
>>> df= pd.readf= pd.read_csv('middle_tn_schools.csv')
>>> df.describe()
       name        size  ...  percent_hispanic  Unnamed: 15
count   0.0  347.000000  ...        346.000000   346.000000
mean    NaN    2.968300  ...          2.631214    11.053757
std     NaN    1.690377  ...          3.106815    11.869415
min     NaN    0.000000  ...          0.000000     0.000000
25%     NaN    2.000000  ...          0.725000     3.800000
50%     NaN    3.000000  ...          1.600000     6.400000
75%     NaN    4.000000  ...          3.100000    13.775000
max     NaN    5.000000  ...         21.100000    65.200000

[8 rows x 14 columns]
>>> df[['reduced_lunch','school_rating']].groupby(['school_rating']).describe().unstack()
                      school_rating               
reduced_lunch  count  Allendale Elementary School       1.0
                      Anderson Elementary               1.0
                      Avoca Elementary                  1.0
                      Bailey Middle                     1.0
                      Barfield Elementary               1.0
                                                      ...  
               max    Winfree Bryant Middle School    611.0
                      Winstead Elementary School      515.0
                      Woodland Elementary             424.0
                      Woodland Middle School          866.0
                      Wright Middle                   829.0
Length: 2728, dtype: float64
>>> df[['reduced_lunch','school_rating']].corr()
               reduced_lunch
reduced_lunch            1.0
>>> #Ejercicio 2
>>> from sklearn.datasets import load_diabetes
>>> dataset= load_diabetes()
>>> dataset
{'data': array([[ 0.03807591,  0.05068012,  0.06169621, ..., -0.00259226,
         0.01990842, -0.01764613],
       [-0.00188202, -0.04464164, -0.05147406, ..., -0.03949338,
        -0.06832974, -0.09220405],
       [ 0.08529891,  0.05068012,  0.04445121, ..., -0.00259226,
         0.00286377, -0.02593034],
       ...,
       [ 0.04170844,  0.05068012, -0.01590626, ..., -0.01107952,
        -0.04687948,  0.01549073],
       [-0.04547248, -0.04464164,  0.03906215, ...,  0.02655962,
         0.04452837, -0.02593034],
       [-0.04547248, -0.04464164, -0.0730303 , ..., -0.03949338,
        -0.00421986,  0.00306441]]), 'target': array([151.,  75., 141., 206., 135.,  97., 138.,  63., 110., 310., 101.,
        69., 179., 185., 118., 171., 166., 144.,  97., 168.,  68.,  49.,
        68., 245., 184., 202., 137.,  85., 131., 283., 129.,  59., 341.,
        87.,  65., 102., 265., 276., 252.,  90., 100.,  55.,  61.,  92.,
       259.,  53., 190., 142.,  75., 142., 155., 225.,  59., 104., 182.,
       128.,  52.,  37., 170., 170.,  61., 144.,  52., 128.,  71., 163.,
       150.,  97., 160., 178.,  48., 270., 202., 111.,  85.,  42., 170.,
       200., 252., 113., 143.,  51.,  52., 210.,  65., 141.,  55., 134.,
        42., 111.,  98., 164.,  48.,  96.,  90., 162., 150., 279.,  92.,
        83., 128., 102., 302., 198.,  95.,  53., 134., 144., 232.,  81.,
       104.,  59., 246., 297., 258., 229., 275., 281., 179., 200., 200.,
       173., 180.,  84., 121., 161.,  99., 109., 115., 268., 274., 158.,
       107.,  83., 103., 272.,  85., 280., 336., 281., 118., 317., 235.,
        60., 174., 259., 178., 128.,  96., 126., 288.,  88., 292.,  71.,
       197., 186.,  25.,  84.,  96., 195.,  53., 217., 172., 131., 214.,
        59.,  70., 220., 268., 152.,  47.,  74., 295., 101., 151., 127.,
       237., 225.,  81., 151., 107.,  64., 138., 185., 265., 101., 137.,
       143., 141.,  79., 292., 178.,  91., 116.,  86., 122.,  72., 129.,
       142.,  90., 158.,  39., 196., 222., 277.,  99., 196., 202., 155.,
        77., 191.,  70.,  73.,  49.,  65., 263., 248., 296., 214., 185.,
        78.,  93., 252., 150.,  77., 208.,  77., 108., 160.,  53., 220.,
       154., 259.,  90., 246., 124.,  67.,  72., 257., 262., 275., 177.,
        71.,  47., 187., 125.,  78.,  51., 258., 215., 303., 243.,  91.,
       150., 310., 153., 346.,  63.,  89.,  50.,  39., 103., 308., 116.,
       145.,  74.,  45., 115., 264.,  87., 202., 127., 182., 241.,  66.,
        94., 283.,  64., 102., 200., 265.,  94., 230., 181., 156., 233.,
        60., 219.,  80.,  68., 332., 248.,  84., 200.,  55.,  85.,  89.,
        31., 129.,  83., 275.,  65., 198., 236., 253., 124.,  44., 172.,
       114., 142., 109., 180., 144., 163., 147.,  97., 220., 190., 109.,
       191., 122., 230., 242., 248., 249., 192., 131., 237.,  78., 135.,
       244., 199., 270., 164.,  72.,  96., 306.,  91., 214.,  95., 216.,
       263., 178., 113., 200., 139., 139.,  88., 148.,  88., 243.,  71.,
        77., 109., 272.,  60.,  54., 221.,  90., 311., 281., 182., 321.,
        58., 262., 206., 233., 242., 123., 167.,  63., 197.,  71., 168.,
       140., 217., 121., 235., 245.,  40.,  52., 104., 132.,  88.,  69.,
       219.,  72., 201., 110.,  51., 277.,  63., 118.,  69., 273., 258.,
        43., 198., 242., 232., 175.,  93., 168., 275., 293., 281.,  72.,
       140., 189., 181., 209., 136., 261., 113., 131., 174., 257.,  55.,
        84.,  42., 146., 212., 233.,  91., 111., 152., 120.,  67., 310.,
        94., 183.,  66., 173.,  72.,  49.,  64.,  48., 178., 104., 132.,
       220.,  57.]), 'frame': None, 'DESCR': '.. _diabetes_dataset:\n\nDiabetes dataset\n----------------\n\nTen baseline variables, age, sex, body mass index, average blood\npressure, and six blood serum measurements were obtained for each of n =\n442 diabetes patients, as well as the response of interest, a\nquantitative measure of disease progression one year after baseline.\n\n**Data Set Characteristics:**\n\n  :Number of Instances: 442\n\n  :Number of Attributes: First 10 columns are numeric predictive values\n\n  :Target: Column 11 is a quantitative measure of disease progression one year after baseline\n\n  :Attribute Information:\n      - age     age in years\n      - sex\n      - bmi     body mass index\n      - bp      average blood pressure\n      - s1      tc, total serum cholesterol\n      - s2      ldl, low-density lipoproteins\n      - s3      hdl, high-density lipoproteins\n      - s4      tch, total cholesterol / HDL\n      - s5      ltg, possibly log of serum triglycerides level\n      - s6      glu, blood sugar level\n\nNote: Each of these 10 feature variables have been mean centered and scaled by the standard deviation times `n_samples` (i.e. the sum of squares of each column totals 1).\n\nSource URL:\nhttps://www4.stat.ncsu.edu/~boos/var.select/diabetes.html\n\nFor more information see:\nBradley Efron, Trevor Hastie, Iain Johnstone and Robert Tibshirani (2004) "Least Angle Regression," Annals of Statistics (with discussion), 407-499.\n(https://web.stanford.edu/~hastie/Papers/LARS/LeastAngle_2002.pdf)', 'feature_names': ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6'], 'data_filename': 'diabetes_data.csv.gz', 'target_filename': 'diabetes_target.csv.gz', 'data_module': 'sklearn.datasets.data'}
>>> dataset.target
array([151.,  75., 141., 206., 135.,  97., 138.,  63., 110., 310., 101.,
        69., 179., 185., 118., 171., 166., 144.,  97., 168.,  68.,  49.,
        68., 245., 184., 202., 137.,  85., 131., 283., 129.,  59., 341.,
        87.,  65., 102., 265., 276., 252.,  90., 100.,  55.,  61.,  92.,
       259.,  53., 190., 142.,  75., 142., 155., 225.,  59., 104., 182.,
       128.,  52.,  37., 170., 170.,  61., 144.,  52., 128.,  71., 163.,
       150.,  97., 160., 178.,  48., 270., 202., 111.,  85.,  42., 170.,
       200., 252., 113., 143.,  51.,  52., 210.,  65., 141.,  55., 134.,
        42., 111.,  98., 164.,  48.,  96.,  90., 162., 150., 279.,  92.,
        83., 128., 102., 302., 198.,  95.,  53., 134., 144., 232.,  81.,
       104.,  59., 246., 297., 258., 229., 275., 281., 179., 200., 200.,
       173., 180.,  84., 121., 161.,  99., 109., 115., 268., 274., 158.,
       107.,  83., 103., 272.,  85., 280., 336., 281., 118., 317., 235.,
        60., 174., 259., 178., 128.,  96., 126., 288.,  88., 292.,  71.,
       197., 186.,  25.,  84.,  96., 195.,  53., 217., 172., 131., 214.,
        59.,  70., 220., 268., 152.,  47.,  74., 295., 101., 151., 127.,
       237., 225.,  81., 151., 107.,  64., 138., 185., 265., 101., 137.,
       143., 141.,  79., 292., 178.,  91., 116.,  86., 122.,  72., 129.,
       142.,  90., 158.,  39., 196., 222., 277.,  99., 196., 202., 155.,
        77., 191.,  70.,  73.,  49.,  65., 263., 248., 296., 214., 185.,
        78.,  93., 252., 150.,  77., 208.,  77., 108., 160.,  53., 220.,
       154., 259.,  90., 246., 124.,  67.,  72., 257., 262., 275., 177.,
        71.,  47., 187., 125.,  78.,  51., 258., 215., 303., 243.,  91.,
       150., 310., 153., 346.,  63.,  89.,  50.,  39., 103., 308., 116.,
       145.,  74.,  45., 115., 264.,  87., 202., 127., 182., 241.,  66.,
        94., 283.,  64., 102., 200., 265.,  94., 230., 181., 156., 233.,
        60., 219.,  80.,  68., 332., 248.,  84., 200.,  55.,  85.,  89.,
        31., 129.,  83., 275.,  65., 198., 236., 253., 124.,  44., 172.,
       114., 142., 109., 180., 144., 163., 147.,  97., 220., 190., 109.,
       191., 122., 230., 242., 248., 249., 192., 131., 237.,  78., 135.,
       244., 199., 270., 164.,  72.,  96., 306.,  91., 214.,  95., 216.,
       263., 178., 113., 200., 139., 139.,  88., 148.,  88., 243.,  71.,
        77., 109., 272.,  60.,  54., 221.,  90., 311., 281., 182., 321.,
        58., 262., 206., 233., 242., 123., 167.,  63., 197.,  71., 168.,
       140., 217., 121., 235., 245.,  40.,  52., 104., 132.,  88.,  69.,
       219.,  72., 201., 110.,  51., 277.,  63., 118.,  69., 273., 258.,
        43., 198., 242., 232., 175.,  93., 168., 275., 293., 281.,  72.,
       140., 189., 181., 209., 136., 261., 113., 131., 174., 257.,  55.,
        84.,  42., 146., 212., 233.,  91., 111., 152., 120.,  67., 310.,
        94., 183.,  66., 173.,  72.,  49.,  64.,  48., 178., 104., 132.,
       220.,  57.])
>>> dataset['feature_names']
['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
>>> import pandas as pd
>>> import numpy as np
>>> df= pd.Dataframe(data= np.c_[dataset['data'],dataset['target'], columns= dataset['feature_names']+['target']])
SyntaxError: invalid syntax
>>> df= pd.Dataframe(data= np.c_[dataset['data'],dataset['target']], columns= dataset['feature_names']+['target'])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    df= pd.Dataframe(data= np.c_[dataset['data'],dataset['target']], columns= dataset['feature_names']+['target'])
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/__init__.py", line 261, in __getattr__
    raise AttributeError(f"module 'pandas' has no attribute '{name}'")
AttributeError: module 'pandas' has no attribute 'Dataframe'
>>> df= pd.DataFrame(data= np.c_[dataset['data'],dataset['target']], columns= dataset['feature_names']+['target'])
>>> df
          age       sex       bmi  ...        s5        s6  target
0    0.038076  0.050680  0.061696  ...  0.019908 -0.017646   151.0
1   -0.001882 -0.044642 -0.051474  ... -0.068330 -0.092204    75.0
2    0.085299  0.050680  0.044451  ...  0.002864 -0.025930   141.0
3   -0.089063 -0.044642 -0.011595  ...  0.022692 -0.009362   206.0
4    0.005383 -0.044642 -0.036385  ... -0.031991 -0.046641   135.0
..        ...       ...       ...  ...       ...       ...     ...
437  0.041708  0.050680  0.019662  ...  0.031193  0.007207   178.0
438 -0.005515  0.050680 -0.015906  ... -0.018118  0.044485   104.0
439  0.041708  0.050680 -0.015906  ... -0.046879  0.015491   132.0
440 -0.045472 -0.044642  0.039062  ...  0.044528 -0.025930   220.0
441 -0.045472 -0.044642 -0.073030  ... -0.004220  0.003064    57.0

[442 rows x 11 columns]
>>> df.isnull().any()
age       False
sex       False
bmi       False
bp        False
s1        False
s2        False
s3        False
s4        False
s5        False
s6        False
target    False
dtype: bool
>>> import matplotlib.pyplot as plt
>>> for column in df():
	plt.figure()
	df.boxplot([column])

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    for column in df():
TypeError: 'DataFrame' object is not callable
>>> for column in df:
	plt.figure()
	df.boxplot([column])

<Figure size 1280x960 with 0 Axes>
<AxesSubplot:>
<Figure size 1280x960 with 0 Axes>
<AxesSubplot:>
<Figure size 1280x960 with 0 Axes>
<AxesSubplot:>
<Figure size 1280x960 with 0 Axes>
<AxesSubplot:>
<Figure size 1280x960 with 0 Axes>
<AxesSubplot:>
<Figure size 1280x960 with 0 Axes>
<AxesSubplot:>
<Figure size 1280x960 with 0 Axes>
<AxesSubplot:>
<Figure size 1280x960 with 0 Axes>
<AxesSubplot:>
<Figure size 1280x960 with 0 Axes>
<AxesSubplot:>
<Figure size 1280x960 with 0 Axes>
<AxesSubplot:>
<Figure size 1280x960 with 0 Axes>
<AxesSubplot:>
>>> plt.show()
>>> 
>>> #Ejercicio 3
>>> os.chdir('/Users/robertogarcia/Documents/Ciencia de Datos/Machine Learning')
>>> df= pd.read_csv('mtcars.csv')
>>> df.describe()
             mpg        cyl        disp  ...         am       gear     carb
count  32.000000  32.000000   32.000000  ...  32.000000  32.000000  32.0000
mean   20.090625   6.187500  230.721875  ...   0.406250   3.687500   2.8125
std     6.026948   1.785922  123.938694  ...   0.498991   0.737804   1.6152
min    10.400000   4.000000   71.100000  ...   0.000000   3.000000   1.0000
25%    15.425000   4.000000  120.825000  ...   0.000000   3.000000   2.0000
50%    19.200000   6.000000  196.300000  ...   0.000000   4.000000   2.0000
75%    22.800000   8.000000  326.000000  ...   1.000000   4.000000   4.0000
max    33.900000   8.000000  472.000000  ...   1.000000   5.000000   8.0000

[8 rows x 11 columns]
>>> pd.target
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    pd.target
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/__init__.py", line 261, in __getattr__
    raise AttributeError(f"module 'pandas' has no attribute '{name}'")
AttributeError: module 'pandas' has no attribute 'target'
>>> df.target
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    df.target
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/generic.py", line 5583, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'target'
>>> df[['hp']].groupby(['hp']).describe().unstack()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    df[['hp']].groupby(['hp']).describe().unstack()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/groupby/groupby.py", line 2312, in describe
    result = self.apply(lambda x: x.describe(**kwargs))
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/groupby/groupby.py", line 1414, in apply
    result = self._python_apply_general(f, self._selected_obj)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/groupby/groupby.py", line 1455, in _python_apply_general
    values, mutated = self.grouper.apply(f, data, self.axis)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/groupby/ops.py", line 761, in apply
    res = f(group)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/groupby/groupby.py", line 2312, in <lambda>
    result = self.apply(lambda x: x.describe(**kwargs))
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/generic.py", line 10235, in describe
    return describe_ndframe(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/describe.py", line 87, in describe_ndframe
    describer = DataFrameDescriber(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/describe.py", line 164, in __init__
    raise ValueError("Cannot describe a DataFrame without columns")
ValueError: Cannot describe a DataFrame without columns
>>> df[['hp']].corr()
     hp
hp  1.0
>>> for column in df:
	plt.figure()
	df.boxplot([column])

<Figure size 1280x960 with 0 Axes>
Traceback (most recent call last):
  File "<pyshell#44>", line 3, in <module>
    df.boxplot([column])
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/plotting/_core.py", line 511, in boxplot_frame
    return plot_backend.boxplot_frame(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/plotting/_matplotlib/boxplot.py", line 425, in boxplot_frame
    ax = boxplot(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/plotting/_matplotlib/boxplot.py", line 402, in boxplot
    data = data[columns]
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/frame.py", line 3512, in __getitem__
    indexer = self.columns._get_indexer_strict(key, "columns")[1]
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 5782, in _get_indexer_strict
    self._raise_if_missing(keyarr, indexer, axis_name)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pandas/core/indexes/base.py", line 5842, in _raise_if_missing
    raise KeyError(f"None of [{key}] are in the [{axis_name}]")
KeyError: "None of [Index(['model'], dtype='object')] are in the [columns]"
>>> df.hp.describe()
count     32.000000
mean     146.687500
std       68.562868
min       52.000000
25%       96.500000
50%      123.000000
75%      180.000000
max      335.000000
Name: hp, dtype: float64
>>> ordered=df1.sort_values(by=['hp'], ascending=False)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    ordered=df1.sort_values(by=['hp'], ascending=False)
NameError: name 'df1' is not defined
>>> ordered=df.sort_values(by=['hp'], ascending=False)
>>> ordered=ordered.reset_index(drop=True)
>>> ordered
                  model   mpg  cyl   disp   hp  ...   qsec  vs  am  gear  carb
0         Maserati Bora  15.0    8  301.0  335  ...  14.60   0   1     5     8
1        Ford Pantera L  15.8    8  351.0  264  ...  14.50   0   1     5     4
2            Duster 360  14.3    8  360.0  245  ...  15.84   0   0     3     4
3            Camaro Z28  13.3    8  350.0  245  ...  15.41   0   0     3     4
4     Chrysler Imperial  14.7    8  440.0  230  ...  17.42   0   0     3     4
5   Lincoln Continental  10.4    8  460.0  215  ...  17.82   0   0     3     4
6    Cadillac Fleetwood  10.4    8  472.0  205  ...  17.98   0   0     3     4
7           Merc 450SLC  15.2    8  275.8  180  ...  18.00   0   0     3     3
8            Merc 450SE  16.4    8  275.8  180  ...  17.40   0   0     3     3
9            Merc 450SL  17.3    8  275.8  180  ...  17.60   0   0     3     3
10         Ferrari Dino  19.7    6  145.0  175  ...  15.50   0   1     5     6
11    Hornet Sportabout  18.7    8  360.0  175  ...  17.02   0   0     3     2
12     Pontiac Firebird  19.2    8  400.0  175  ...  17.05   0   0     3     2
13          AMC Javelin  15.2    8  304.0  150  ...  17.30   0   0     3     2
14     Dodge Challenger  15.5    8  318.0  150  ...  16.87   0   0     3     2
15            Merc 280C  17.8    6  167.6  123  ...  18.90   1   0     4     4
16             Merc 280  19.2    6  167.6  123  ...  18.30   1   0     4     4
17         Lotus Europa  30.4    4   95.1  113  ...  16.90   1   1     5     2
18            Mazda RX4  21.0    6  160.0  110  ...  16.46   0   1     4     4
19        Mazda RX4 Wag  21.0    6  160.0  110  ...  17.02   0   1     4     4
20       Hornet 4 Drive  21.4    6  258.0  110  ...  19.44   1   0     3     1
21           Volvo 142E  21.4    4  121.0  109  ...  18.60   1   1     4     2
22              Valiant  18.1    6  225.0  105  ...  20.22   1   0     3     1
23        Toyota Corona  21.5    4  120.1   97  ...  20.01   1   0     3     1
24             Merc 230  22.8    4  140.8   95  ...  22.90   1   0     4     2
25           Datsun 710  22.8    4  108.0   93  ...  18.61   1   1     4     1
26        Porsche 914-2  26.0    4  120.3   91  ...  16.70   0   1     5     2
27             Fiat 128  32.4    4   78.7   66  ...  19.47   1   1     4     1
28            Fiat X1-9  27.3    4   79.0   66  ...  18.90   1   1     4     1
29       Toyota Corolla  33.9    4   71.1   65  ...  19.90   1   1     4     1
30            Merc 240D  24.4    4  146.7   62  ...  20.00   1   0     4     2
31          Honda Civic  30.4    4   75.7   52  ...  18.52   1   1     4     2

[32 rows x 12 columns]
>>> AvgHP=ordered.loc[(ordered['hp'] >= 109) & (ordered['hp'] <= 180)]
>>> AvgHP=AvgHP.reset_index(drop=True)
>>> AvgHP
                model   mpg  cyl   disp   hp  ...   qsec  vs  am  gear  carb
0         Merc 450SLC  15.2    8  275.8  180  ...  18.00   0   0     3     3
1          Merc 450SE  16.4    8  275.8  180  ...  17.40   0   0     3     3
2          Merc 450SL  17.3    8  275.8  180  ...  17.60   0   0     3     3
3        Ferrari Dino  19.7    6  145.0  175  ...  15.50   0   1     5     6
4   Hornet Sportabout  18.7    8  360.0  175  ...  17.02   0   0     3     2
5    Pontiac Firebird  19.2    8  400.0  175  ...  17.05   0   0     3     2
6         AMC Javelin  15.2    8  304.0  150  ...  17.30   0   0     3     2
7    Dodge Challenger  15.5    8  318.0  150  ...  16.87   0   0     3     2
8           Merc 280C  17.8    6  167.6  123  ...  18.90   1   0     4     4
9            Merc 280  19.2    6  167.6  123  ...  18.30   1   0     4     4
10       Lotus Europa  30.4    4   95.1  113  ...  16.90   1   1     5     2
11          Mazda RX4  21.0    6  160.0  110  ...  16.46   0   1     4     4
12      Mazda RX4 Wag  21.0    6  160.0  110  ...  17.02   0   1     4     4
13     Hornet 4 Drive  21.4    6  258.0  110  ...  19.44   1   0     3     1
14         Volvo 142E  21.4    4  121.0  109  ...  18.60   1   1     4     2

[15 rows x 12 columns]
>>> AvgHP.describe()
             mpg        cyl        disp  ...         am       gear       carb
count  15.000000  15.000000   15.000000  ...  15.000000  15.000000  15.000000
mean   19.293333   6.666667  232.246667  ...   0.333333   3.600000   2.933333
std     3.789736   1.447494   92.933439  ...   0.487950   0.736788   1.279881
min    15.200000   4.000000   95.100000  ...   0.000000   3.000000   1.000000
25%    16.850000   6.000000  160.000000  ...   0.000000   3.000000   2.000000
50%    19.200000   6.000000  258.000000  ...   0.000000   3.000000   3.000000
75%    21.000000   8.000000  289.900000  ...   1.000000   4.000000   4.000000
max    30.400000   8.000000  400.000000  ...   1.000000   5.000000   6.000000

[8 rows x 11 columns]
>>> corr2= AvgHP.corr()
>>> sns.heatmap(corr2, cmap="Greens")
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    sns.heatmap(corr2, cmap="Greens")
NameError: name 'sns' is not defined
>>> import seaborn as sns
>>> sns.heatmap(corr2, cmap="Greens")
<AxesSubplot:>
>>> plt.show()
>>> 