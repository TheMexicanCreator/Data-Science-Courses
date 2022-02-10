{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cfb8a988-ac5f-4695-8afe-fc557845cbd2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'data': array([[5.1, 3.5, 1.4, 0.2],\n",
      "       [4.9, 3. , 1.4, 0.2],\n",
      "       [4.7, 3.2, 1.3, 0.2],\n",
      "       [4.6, 3.1, 1.5, 0.2],\n",
      "       [5. , 3.6, 1.4, 0.2],\n",
      "       [5.4, 3.9, 1.7, 0.4],\n",
      "       [4.6, 3.4, 1.4, 0.3],\n",
      "       [5. , 3.4, 1.5, 0.2],\n",
      "       [4.4, 2.9, 1.4, 0.2],\n",
      "       [4.9, 3.1, 1.5, 0.1],\n",
      "       [5.4, 3.7, 1.5, 0.2],\n",
      "       [4.8, 3.4, 1.6, 0.2],\n",
      "       [4.8, 3. , 1.4, 0.1],\n",
      "       [4.3, 3. , 1.1, 0.1],\n",
      "       [5.8, 4. , 1.2, 0.2],\n",
      "       [5.7, 4.4, 1.5, 0.4],\n",
      "       [5.4, 3.9, 1.3, 0.4],\n",
      "       [5.1, 3.5, 1.4, 0.3],\n",
      "       [5.7, 3.8, 1.7, 0.3],\n",
      "       [5.1, 3.8, 1.5, 0.3],\n",
      "       [5.4, 3.4, 1.7, 0.2],\n",
      "       [5.1, 3.7, 1.5, 0.4],\n",
      "       [4.6, 3.6, 1. , 0.2],\n",
      "       [5.1, 3.3, 1.7, 0.5],\n",
      "       [4.8, 3.4, 1.9, 0.2],\n",
      "       [5. , 3. , 1.6, 0.2],\n",
      "       [5. , 3.4, 1.6, 0.4],\n",
      "       [5.2, 3.5, 1.5, 0.2],\n",
      "       [5.2, 3.4, 1.4, 0.2],\n",
      "       [4.7, 3.2, 1.6, 0.2],\n",
      "       [4.8, 3.1, 1.6, 0.2],\n",
      "       [5.4, 3.4, 1.5, 0.4],\n",
      "       [5.2, 4.1, 1.5, 0.1],\n",
      "       [5.5, 4.2, 1.4, 0.2],\n",
      "       [4.9, 3.1, 1.5, 0.2],\n",
      "       [5. , 3.2, 1.2, 0.2],\n",
      "       [5.5, 3.5, 1.3, 0.2],\n",
      "       [4.9, 3.6, 1.4, 0.1],\n",
      "       [4.4, 3. , 1.3, 0.2],\n",
      "       [5.1, 3.4, 1.5, 0.2],\n",
      "       [5. , 3.5, 1.3, 0.3],\n",
      "       [4.5, 2.3, 1.3, 0.3],\n",
      "       [4.4, 3.2, 1.3, 0.2],\n",
      "       [5. , 3.5, 1.6, 0.6],\n",
      "       [5.1, 3.8, 1.9, 0.4],\n",
      "       [4.8, 3. , 1.4, 0.3],\n",
      "       [5.1, 3.8, 1.6, 0.2],\n",
      "       [4.6, 3.2, 1.4, 0.2],\n",
      "       [5.3, 3.7, 1.5, 0.2],\n",
      "       [5. , 3.3, 1.4, 0.2],\n",
      "       [7. , 3.2, 4.7, 1.4],\n",
      "       [6.4, 3.2, 4.5, 1.5],\n",
      "       [6.9, 3.1, 4.9, 1.5],\n",
      "       [5.5, 2.3, 4. , 1.3],\n",
      "       [6.5, 2.8, 4.6, 1.5],\n",
      "       [5.7, 2.8, 4.5, 1.3],\n",
      "       [6.3, 3.3, 4.7, 1.6],\n",
      "       [4.9, 2.4, 3.3, 1. ],\n",
      "       [6.6, 2.9, 4.6, 1.3],\n",
      "       [5.2, 2.7, 3.9, 1.4],\n",
      "       [5. , 2. , 3.5, 1. ],\n",
      "       [5.9, 3. , 4.2, 1.5],\n",
      "       [6. , 2.2, 4. , 1. ],\n",
      "       [6.1, 2.9, 4.7, 1.4],\n",
      "       [5.6, 2.9, 3.6, 1.3],\n",
      "       [6.7, 3.1, 4.4, 1.4],\n",
      "       [5.6, 3. , 4.5, 1.5],\n",
      "       [5.8, 2.7, 4.1, 1. ],\n",
      "       [6.2, 2.2, 4.5, 1.5],\n",
      "       [5.6, 2.5, 3.9, 1.1],\n",
      "       [5.9, 3.2, 4.8, 1.8],\n",
      "       [6.1, 2.8, 4. , 1.3],\n",
      "       [6.3, 2.5, 4.9, 1.5],\n",
      "       [6.1, 2.8, 4.7, 1.2],\n",
      "       [6.4, 2.9, 4.3, 1.3],\n",
      "       [6.6, 3. , 4.4, 1.4],\n",
      "       [6.8, 2.8, 4.8, 1.4],\n",
      "       [6.7, 3. , 5. , 1.7],\n",
      "       [6. , 2.9, 4.5, 1.5],\n",
      "       [5.7, 2.6, 3.5, 1. ],\n",
      "       [5.5, 2.4, 3.8, 1.1],\n",
      "       [5.5, 2.4, 3.7, 1. ],\n",
      "       [5.8, 2.7, 3.9, 1.2],\n",
      "       [6. , 2.7, 5.1, 1.6],\n",
      "       [5.4, 3. , 4.5, 1.5],\n",
      "       [6. , 3.4, 4.5, 1.6],\n",
      "       [6.7, 3.1, 4.7, 1.5],\n",
      "       [6.3, 2.3, 4.4, 1.3],\n",
      "       [5.6, 3. , 4.1, 1.3],\n",
      "       [5.5, 2.5, 4. , 1.3],\n",
      "       [5.5, 2.6, 4.4, 1.2],\n",
      "       [6.1, 3. , 4.6, 1.4],\n",
      "       [5.8, 2.6, 4. , 1.2],\n",
      "       [5. , 2.3, 3.3, 1. ],\n",
      "       [5.6, 2.7, 4.2, 1.3],\n",
      "       [5.7, 3. , 4.2, 1.2],\n",
      "       [5.7, 2.9, 4.2, 1.3],\n",
      "       [6.2, 2.9, 4.3, 1.3],\n",
      "       [5.1, 2.5, 3. , 1.1],\n",
      "       [5.7, 2.8, 4.1, 1.3],\n",
      "       [6.3, 3.3, 6. , 2.5],\n",
      "       [5.8, 2.7, 5.1, 1.9],\n",
      "       [7.1, 3. , 5.9, 2.1],\n",
      "       [6.3, 2.9, 5.6, 1.8],\n",
      "       [6.5, 3. , 5.8, 2.2],\n",
      "       [7.6, 3. , 6.6, 2.1],\n",
      "       [4.9, 2.5, 4.5, 1.7],\n",
      "       [7.3, 2.9, 6.3, 1.8],\n",
      "       [6.7, 2.5, 5.8, 1.8],\n",
      "       [7.2, 3.6, 6.1, 2.5],\n",
      "       [6.5, 3.2, 5.1, 2. ],\n",
      "       [6.4, 2.7, 5.3, 1.9],\n",
      "       [6.8, 3. , 5.5, 2.1],\n",
      "       [5.7, 2.5, 5. , 2. ],\n",
      "       [5.8, 2.8, 5.1, 2.4],\n",
      "       [6.4, 3.2, 5.3, 2.3],\n",
      "       [6.5, 3. , 5.5, 1.8],\n",
      "       [7.7, 3.8, 6.7, 2.2],\n",
      "       [7.7, 2.6, 6.9, 2.3],\n",
      "       [6. , 2.2, 5. , 1.5],\n",
      "       [6.9, 3.2, 5.7, 2.3],\n",
      "       [5.6, 2.8, 4.9, 2. ],\n",
      "       [7.7, 2.8, 6.7, 2. ],\n",
      "       [6.3, 2.7, 4.9, 1.8],\n",
      "       [6.7, 3.3, 5.7, 2.1],\n",
      "       [7.2, 3.2, 6. , 1.8],\n",
      "       [6.2, 2.8, 4.8, 1.8],\n",
      "       [6.1, 3. , 4.9, 1.8],\n",
      "       [6.4, 2.8, 5.6, 2.1],\n",
      "       [7.2, 3. , 5.8, 1.6],\n",
      "       [7.4, 2.8, 6.1, 1.9],\n",
      "       [7.9, 3.8, 6.4, 2. ],\n",
      "       [6.4, 2.8, 5.6, 2.2],\n",
      "       [6.3, 2.8, 5.1, 1.5],\n",
      "       [6.1, 2.6, 5.6, 1.4],\n",
      "       [7.7, 3. , 6.1, 2.3],\n",
      "       [6.3, 3.4, 5.6, 2.4],\n",
      "       [6.4, 3.1, 5.5, 1.8],\n",
      "       [6. , 3. , 4.8, 1.8],\n",
      "       [6.9, 3.1, 5.4, 2.1],\n",
      "       [6.7, 3.1, 5.6, 2.4],\n",
      "       [6.9, 3.1, 5.1, 2.3],\n",
      "       [5.8, 2.7, 5.1, 1.9],\n",
      "       [6.8, 3.2, 5.9, 2.3],\n",
      "       [6.7, 3.3, 5.7, 2.5],\n",
      "       [6.7, 3. , 5.2, 2.3],\n",
      "       [6.3, 2.5, 5. , 1.9],\n",
      "       [6.5, 3. , 5.2, 2. ],\n",
      "       [6.2, 3.4, 5.4, 2.3],\n",
      "       [5.9, 3. , 5.1, 1.8]]), 'target': array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\n",
      "       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\n",
      "       0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\n",
      "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\n",
      "       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,\n",
      "       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,\n",
      "       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), 'frame': None, 'target_names': array(['setosa', 'versicolor', 'virginica'], dtype='<U10'), 'DESCR': '.. _iris_dataset:\\n\\nIris plants dataset\\n--------------------\\n\\n**Data Set Characteristics:**\\n\\n    :Number of Instances: 150 (50 in each of three classes)\\n    :Number of Attributes: 4 numeric, predictive attributes and the class\\n    :Attribute Information:\\n        - sepal length in cm\\n        - sepal width in cm\\n        - petal length in cm\\n        - petal width in cm\\n        - class:\\n                - Iris-Setosa\\n                - Iris-Versicolour\\n                - Iris-Virginica\\n                \\n    :Summary Statistics:\\n\\n    ============== ==== ==== ======= ===== ====================\\n                    Min  Max   Mean    SD   Class Correlation\\n    ============== ==== ==== ======= ===== ====================\\n    sepal length:   4.3  7.9   5.84   0.83    0.7826\\n    sepal width:    2.0  4.4   3.05   0.43   -0.4194\\n    petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)\\n    petal width:    0.1  2.5   1.20   0.76    0.9565  (high!)\\n    ============== ==== ==== ======= ===== ====================\\n\\n    :Missing Attribute Values: None\\n    :Class Distribution: 33.3% for each of 3 classes.\\n    :Creator: R.A. Fisher\\n    :Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)\\n    :Date: July, 1988\\n\\nThe famous Iris database, first used by Sir R.A. Fisher. The dataset is taken\\nfrom Fisher\\'s paper. Note that it\\'s the same as in R, but not as in the UCI\\nMachine Learning Repository, which has two wrong data points.\\n\\nThis is perhaps the best known database to be found in the\\npattern recognition literature.  Fisher\\'s paper is a classic in the field and\\nis referenced frequently to this day.  (See Duda & Hart, for example.)  The\\ndata set contains 3 classes of 50 instances each, where each class refers to a\\ntype of iris plant.  One class is linearly separable from the other 2; the\\nlatter are NOT linearly separable from each other.\\n\\n.. topic:: References\\n\\n   - Fisher, R.A. \"The use of multiple measurements in taxonomic problems\"\\n     Annual Eugenics, 7, Part II, 179-188 (1936); also in \"Contributions to\\n     Mathematical Statistics\" (John Wiley, NY, 1950).\\n   - Duda, R.O., & Hart, P.E. (1973) Pattern Classification and Scene Analysis.\\n     (Q327.D83) John Wiley & Sons.  ISBN 0-471-22361-1.  See page 218.\\n   - Dasarathy, B.V. (1980) \"Nosing Around the Neighborhood: A New System\\n     Structure and Classification Rule for Recognition in Partially Exposed\\n     Environments\".  IEEE Transactions on Pattern Analysis and Machine\\n     Intelligence, Vol. PAMI-2, No. 1, 67-71.\\n   - Gates, G.W. (1972) \"The Reduced Nearest Neighbor Rule\".  IEEE Transactions\\n     on Information Theory, May 1972, 431-433.\\n   - See also: 1988 MLC Proceedings, 54-64.  Cheeseman et al\"s AUTOCLASS II\\n     conceptual clustering system finds 3 classes in the data.\\n   - Many, many more ...', 'feature_names': ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'], 'filename': 'iris.csv', 'data_module': 'sklearn.datasets.data'}\n"
     ]
    }
   ],
   "source": [
    "from sklearn.datasets import load_iris\n",
    "iris_data= load_iris()\n",
    "print(iris_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "166ca505-bfe0-43cf-83cb-bd5821334172",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_input= iris_data.data\n",
    "data_output= iris_data.target"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b192aa3c-7107-48c6-9500-b3ffa5a52f70",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[5.1 3.5 1.4 0.2]\n",
      " [4.9 3.  1.4 0.2]\n",
      " [4.7 3.2 1.3 0.2]\n",
      " [4.6 3.1 1.5 0.2]\n",
      " [5.  3.6 1.4 0.2]\n",
      " [5.4 3.9 1.7 0.4]\n",
      " [4.6 3.4 1.4 0.3]\n",
      " [5.  3.4 1.5 0.2]\n",
      " [4.4 2.9 1.4 0.2]\n",
      " [4.9 3.1 1.5 0.1]\n",
      " [5.4 3.7 1.5 0.2]\n",
      " [4.8 3.4 1.6 0.2]\n",
      " [4.8 3.  1.4 0.1]\n",
      " [4.3 3.  1.1 0.1]\n",
      " [5.8 4.  1.2 0.2]\n",
      " [5.7 4.4 1.5 0.4]\n",
      " [5.4 3.9 1.3 0.4]\n",
      " [5.1 3.5 1.4 0.3]\n",
      " [5.7 3.8 1.7 0.3]\n",
      " [5.1 3.8 1.5 0.3]\n",
      " [5.4 3.4 1.7 0.2]\n",
      " [5.1 3.7 1.5 0.4]\n",
      " [4.6 3.6 1.  0.2]\n",
      " [5.1 3.3 1.7 0.5]\n",
      " [4.8 3.4 1.9 0.2]\n",
      " [5.  3.  1.6 0.2]\n",
      " [5.  3.4 1.6 0.4]\n",
      " [5.2 3.5 1.5 0.2]\n",
      " [5.2 3.4 1.4 0.2]\n",
      " [4.7 3.2 1.6 0.2]\n",
      " [4.8 3.1 1.6 0.2]\n",
      " [5.4 3.4 1.5 0.4]\n",
      " [5.2 4.1 1.5 0.1]\n",
      " [5.5 4.2 1.4 0.2]\n",
      " [4.9 3.1 1.5 0.2]\n",
      " [5.  3.2 1.2 0.2]\n",
      " [5.5 3.5 1.3 0.2]\n",
      " [4.9 3.6 1.4 0.1]\n",
      " [4.4 3.  1.3 0.2]\n",
      " [5.1 3.4 1.5 0.2]\n",
      " [5.  3.5 1.3 0.3]\n",
      " [4.5 2.3 1.3 0.3]\n",
      " [4.4 3.2 1.3 0.2]\n",
      " [5.  3.5 1.6 0.6]\n",
      " [5.1 3.8 1.9 0.4]\n",
      " [4.8 3.  1.4 0.3]\n",
      " [5.1 3.8 1.6 0.2]\n",
      " [4.6 3.2 1.4 0.2]\n",
      " [5.3 3.7 1.5 0.2]\n",
      " [5.  3.3 1.4 0.2]\n",
      " [7.  3.2 4.7 1.4]\n",
      " [6.4 3.2 4.5 1.5]\n",
      " [6.9 3.1 4.9 1.5]\n",
      " [5.5 2.3 4.  1.3]\n",
      " [6.5 2.8 4.6 1.5]\n",
      " [5.7 2.8 4.5 1.3]\n",
      " [6.3 3.3 4.7 1.6]\n",
      " [4.9 2.4 3.3 1. ]\n",
      " [6.6 2.9 4.6 1.3]\n",
      " [5.2 2.7 3.9 1.4]\n",
      " [5.  2.  3.5 1. ]\n",
      " [5.9 3.  4.2 1.5]\n",
      " [6.  2.2 4.  1. ]\n",
      " [6.1 2.9 4.7 1.4]\n",
      " [5.6 2.9 3.6 1.3]\n",
      " [6.7 3.1 4.4 1.4]\n",
      " [5.6 3.  4.5 1.5]\n",
      " [5.8 2.7 4.1 1. ]\n",
      " [6.2 2.2 4.5 1.5]\n",
      " [5.6 2.5 3.9 1.1]\n",
      " [5.9 3.2 4.8 1.8]\n",
      " [6.1 2.8 4.  1.3]\n",
      " [6.3 2.5 4.9 1.5]\n",
      " [6.1 2.8 4.7 1.2]\n",
      " [6.4 2.9 4.3 1.3]\n",
      " [6.6 3.  4.4 1.4]\n",
      " [6.8 2.8 4.8 1.4]\n",
      " [6.7 3.  5.  1.7]\n",
      " [6.  2.9 4.5 1.5]\n",
      " [5.7 2.6 3.5 1. ]\n",
      " [5.5 2.4 3.8 1.1]\n",
      " [5.5 2.4 3.7 1. ]\n",
      " [5.8 2.7 3.9 1.2]\n",
      " [6.  2.7 5.1 1.6]\n",
      " [5.4 3.  4.5 1.5]\n",
      " [6.  3.4 4.5 1.6]\n",
      " [6.7 3.1 4.7 1.5]\n",
      " [6.3 2.3 4.4 1.3]\n",
      " [5.6 3.  4.1 1.3]\n",
      " [5.5 2.5 4.  1.3]\n",
      " [5.5 2.6 4.4 1.2]\n",
      " [6.1 3.  4.6 1.4]\n",
      " [5.8 2.6 4.  1.2]\n",
      " [5.  2.3 3.3 1. ]\n",
      " [5.6 2.7 4.2 1.3]\n",
      " [5.7 3.  4.2 1.2]\n",
      " [5.7 2.9 4.2 1.3]\n",
      " [6.2 2.9 4.3 1.3]\n",
      " [5.1 2.5 3.  1.1]\n",
      " [5.7 2.8 4.1 1.3]\n",
      " [6.3 3.3 6.  2.5]\n",
      " [5.8 2.7 5.1 1.9]\n",
      " [7.1 3.  5.9 2.1]\n",
      " [6.3 2.9 5.6 1.8]\n",
      " [6.5 3.  5.8 2.2]\n",
      " [7.6 3.  6.6 2.1]\n",
      " [4.9 2.5 4.5 1.7]\n",
      " [7.3 2.9 6.3 1.8]\n",
      " [6.7 2.5 5.8 1.8]\n",
      " [7.2 3.6 6.1 2.5]\n",
      " [6.5 3.2 5.1 2. ]\n",
      " [6.4 2.7 5.3 1.9]\n",
      " [6.8 3.  5.5 2.1]\n",
      " [5.7 2.5 5.  2. ]\n",
      " [5.8 2.8 5.1 2.4]\n",
      " [6.4 3.2 5.3 2.3]\n",
      " [6.5 3.  5.5 1.8]\n",
      " [7.7 3.8 6.7 2.2]\n",
      " [7.7 2.6 6.9 2.3]\n",
      " [6.  2.2 5.  1.5]\n",
      " [6.9 3.2 5.7 2.3]\n",
      " [5.6 2.8 4.9 2. ]\n",
      " [7.7 2.8 6.7 2. ]\n",
      " [6.3 2.7 4.9 1.8]\n",
      " [6.7 3.3 5.7 2.1]\n",
      " [7.2 3.2 6.  1.8]\n",
      " [6.2 2.8 4.8 1.8]\n",
      " [6.1 3.  4.9 1.8]\n",
      " [6.4 2.8 5.6 2.1]\n",
      " [7.2 3.  5.8 1.6]\n",
      " [7.4 2.8 6.1 1.9]\n",
      " [7.9 3.8 6.4 2. ]\n",
      " [6.4 2.8 5.6 2.2]\n",
      " [6.3 2.8 5.1 1.5]\n",
      " [6.1 2.6 5.6 1.4]\n",
      " [7.7 3.  6.1 2.3]\n",
      " [6.3 3.4 5.6 2.4]\n",
      " [6.4 3.1 5.5 1.8]\n",
      " [6.  3.  4.8 1.8]\n",
      " [6.9 3.1 5.4 2.1]\n",
      " [6.7 3.1 5.6 2.4]\n",
      " [6.9 3.1 5.1 2.3]\n",
      " [5.8 2.7 5.1 1.9]\n",
      " [6.8 3.2 5.9 2.3]\n",
      " [6.7 3.3 5.7 2.5]\n",
      " [6.7 3.  5.2 2.3]\n",
      " [6.3 2.5 5.  1.9]\n",
      " [6.5 3.  5.2 2. ]\n",
      " [6.2 3.4 5.4 2.3]\n",
      " [5.9 3.  5.1 1.8]]\n"
     ]
    }
   ],
   "source": [
    "print(data_input)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c345fb70-bbae-4216-80da-94ea2c2b670f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Train Set        Train Set      \n",
      "[  0   1   3   4   5   6   7   8   9  10  11  12  14  15  16  18  19  21\n",
      "  22  23  25  27  28  29  31  32  33  34  35  37  38  39  40  41  42  43\n",
      "  44  45  47  48  50  51  52  53  54  55  56  57  58  61  62  64  65  66\n",
      "  67  68  69  70  71  72  73  75  76  77  79  80  84  85  86  89  90  91\n",
      "  93  94  95  96  99 100 101 102 104 105 106 108 109 110 111 112 113 114\n",
      " 116 117 118 119 120 121 122 123 124 125 126 127 129 130 131 132 133 134\n",
      " 136 137 139 140 141 142 144 145 146 147 148 149] [  2  13  17  20  24  26  30  36  46  49  59  60  63  74  78  81  82  83\n",
      "  87  88  92  97  98 103 107 115 128 135 138 143]\n",
      "[  0   1   2   3   4   5   6   8  10  11  13  14  15  17  18  20  21  22\n",
      "  23  24  25  26  27  28  30  32  33  34  36  37  38  39  41  42  43  45\n",
      "  46  47  48  49  50  52  53  55  57  58  59  60  61  63  65  66  67  68\n",
      "  69  70  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87\n",
      "  88  89  90  91  92  93  94  96  97  98 100 101 103 105 106 107 108 110\n",
      " 111 112 113 115 116 117 118 119 120 122 124 125 128 129 130 131 133 134\n",
      " 135 136 137 138 139 140 141 143 144 146 147 149] [  7   9  12  16  19  29  31  35  40  44  51  54  56  62  64  71  95  99\n",
      " 102 104 109 114 121 123 126 127 132 142 145 148]\n",
      "[  0   1   2   6   7   8   9  11  12  13  14  15  16  17  19  20  21  24\n",
      "  26  27  28  29  30  31  32  34  35  36  38  39  40  42  43  44  45  46\n",
      "  47  48  49  51  54  55  56  57  58  59  60  62  63  64  65  67  69  70\n",
      "  71  72  74  75  76  78  79  80  81  82  83  85  86  87  88  90  91  92\n",
      "  93  95  97  98  99 100 101 102 103 104 105 107 108 109 110 111 112 114\n",
      " 115 116 117 118 120 121 122 123 124 126 127 128 129 130 131 132 135 136\n",
      " 137 138 139 140 141 142 143 144 145 146 147 148] [  3   4   5  10  18  22  23  25  33  37  41  50  52  53  61  66  68  73\n",
      "  77  84  89  94  96 106 113 119 125 133 134 149]\n",
      "[  0   1   2   3   4   5   7   9  10  11  12  13  15  16  17  18  19  20\n",
      "  21  22  23  24  25  26  29  30  31  32  33  35  36  37  38  39  40  41\n",
      "  42  43  44  46  47  49  50  51  52  53  54  55  56  57  58  59  60  61\n",
      "  62  63  64  65  66  67  68  70  71  72  73  74  76  77  78  80  81  82\n",
      "  83  84  86  87  88  89  92  94  95  96  97  98  99 100 102 103 104 105\n",
      " 106 107 108 109 111 112 113 114 115 119 121 123 125 126 127 128 132 133\n",
      " 134 135 137 138 140 141 142 143 145 146 148 149] [  6   8  14  27  28  34  45  48  69  75  79  85  90  91  93 101 110 116\n",
      " 117 118 120 122 124 129 130 131 136 139 144 147]\n",
      "[  2   3   4   5   6   7   8   9  10  12  13  14  16  17  18  19  20  22\n",
      "  23  24  25  26  27  28  29  30  31  33  34  35  36  37  40  41  44  45\n",
      "  46  48  49  50  51  52  53  54  56  59  60  61  62  63  64  66  68  69\n",
      "  71  73  74  75  77  78  79  81  82  83  84  85  87  88  89  90  91  92\n",
      "  93  94  95  96  97  98  99 101 102 103 104 106 107 109 110 113 114 115\n",
      " 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133\n",
      " 134 135 136 138 139 142 143 144 145 147 148 149] [  0   1  11  15  21  32  38  39  42  43  47  55  57  58  65  67  70  72\n",
      "  76  80  86 100 105 108 111 112 137 140 141 146]\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import KFold\n",
    "kf= KFold(n_splits=5,shuffle=True)\n",
    "print(\"Train Set        Train Set      \")\n",
    "for train_set,test_set in kf.split(data_input):\n",
    "    print(train_set,test_set)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "09c00121-8404-49bb-8b39-1c29f1084a76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1.         0.93333333 1.         0.93333333 0.93333333 0.93333333\n",
      " 0.8        1.         1.         1.        ]\n"
     ]
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "rf_class=  RandomForestClassifier(n_estimators=10)\n",
    "from sklearn.model_selection import cross_val_score\n",
    "print(cross_val_score(rf_class,data_input,data_output,scoring='accuracy',cv=10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "12d9176f-1d7c-444a-a1ee-5c28ce3f8ba5",
   "metadata": {},
   "outputs": [],
   "source": [
    "accuracy= cross_val_score(rf_class,data_input,data_output,scoring='accuracy',cv=10).mean()*100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "f8962836-9f83-4b35-b245-1b14c2f993b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "96.66666666666666\n"
     ]
    }
   ],
   "source": [
    "print(accuracy)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0048f593-4bd4-4fac-9824-e2fb44c1eee6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
