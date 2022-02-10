{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "593985d1-4254-4000-b917-8469406cf6f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn import model_selection\n",
    "from sklearn.ensemble import AdaBoostClassifier\n",
    "df= pd.read_csv('diabetes.csv')\n",
    "array= df.values\n",
    "X= array[:,0:8]\n",
    "Y= array[:,8]\n",
    "seed= 7\n",
    "num_trees= 30"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "957e6b7e-3ac3-443e-a04a-7b31297df856",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.7552802460697198\n"
     ]
    }
   ],
   "source": [
    "kfold= model_selection.KFold(n_splits=10,random_state=seed,shuffle=True)\n",
    "model= AdaBoostClassifier(n_estimators=num_trees,random_state=seed)\n",
    "results= model_selection.cross_val_score(model,X,Y,cv=kfold)\n",
    "print(results.mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "961f85d1-3153-43f2-a7a1-bacc2cd4f2d0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a62111a-a275-4fb1-92fc-e54a6f4c7aab",
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
