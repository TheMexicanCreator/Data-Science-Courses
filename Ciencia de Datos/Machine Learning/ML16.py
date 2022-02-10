{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "74aaa357-a9c8-46f6-a85b-a2761e9b74e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0c3887c7-2304-4ed9-bf58-678b0bafc77b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/Users/robertogarcia/Documents/Ciencia de Datos/Machine Learning'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ef283924-4d80-4c8c-b872-dc22632263cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "os.chdir('/Users/robertogarcia/Documents/Ciencia de Datos/Machine Learning')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "85de0929-fa98-4079-bbd8-8ed5ebd520e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>196</th>\n",
       "      <th>242</th>\n",
       "      <th>3</th>\n",
       "      <th>881250949</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>186</td>\n",
       "      <td>302</td>\n",
       "      <td>3</td>\n",
       "      <td>891717742</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>22</td>\n",
       "      <td>377</td>\n",
       "      <td>1</td>\n",
       "      <td>878887116</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>244</td>\n",
       "      <td>51</td>\n",
       "      <td>2</td>\n",
       "      <td>880606923</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>166</td>\n",
       "      <td>346</td>\n",
       "      <td>1</td>\n",
       "      <td>886397596</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>298</td>\n",
       "      <td>474</td>\n",
       "      <td>4</td>\n",
       "      <td>884182806</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99994</th>\n",
       "      <td>880</td>\n",
       "      <td>476</td>\n",
       "      <td>3</td>\n",
       "      <td>880175444</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99995</th>\n",
       "      <td>716</td>\n",
       "      <td>204</td>\n",
       "      <td>5</td>\n",
       "      <td>879795543</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99996</th>\n",
       "      <td>276</td>\n",
       "      <td>1090</td>\n",
       "      <td>1</td>\n",
       "      <td>874795795</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99997</th>\n",
       "      <td>13</td>\n",
       "      <td>225</td>\n",
       "      <td>2</td>\n",
       "      <td>882399156</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99998</th>\n",
       "      <td>12</td>\n",
       "      <td>203</td>\n",
       "      <td>3</td>\n",
       "      <td>879959583</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>99999 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       196   242  3  881250949\n",
       "0      186   302  3  891717742\n",
       "1       22   377  1  878887116\n",
       "2      244    51  2  880606923\n",
       "3      166   346  1  886397596\n",
       "4      298   474  4  884182806\n",
       "...    ...   ... ..        ...\n",
       "99994  880   476  3  880175444\n",
       "99995  716   204  5  879795543\n",
       "99996  276  1090  1  874795795\n",
       "99997   13   225  2  882399156\n",
       "99998   12   203  3  879959583\n",
       "\n",
       "[99999 rows x 4 columns]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df= pd.read_csv('Recommend.csv')\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2712454b-1230-4f28-b1ed-4467e3c89017",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "n_users= df.user_id.unique().shape[0]\n",
    "n_movies= df.movie_id.unique().shape[0]\n",
    "train_data,test_data= train_test_split(df,testsize=0.25)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0beec033-fc41-49f5-b42e-5cd616f31be5",
   "metadata": {},
   "outputs": [],
   "source": [
    "train_data_matrix= np.zeros((n_users,n_movies))\n",
    "for line in train_data.itertuples():\n",
    "    train_data_matrix[line[1]-1,line[2]-1]= line[3]\n",
    "train_data_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "99ace740-4a26-4034-b0ab-c4f8d04ec15e",
   "metadata": {},
   "outputs": [],
   "source": [
    "test_data_matrix= np.zeros((n_users,n_movies))\n",
    "for line in test_data.itertuples():\n",
    "    test_data_matrix[line[1]-1,line[2]-1]= line[3]\n",
    "test_data_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c44176a-8a7b-42bb-98f8-7b4d05adf349",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import pairwise_distances\n",
    "user_similarity= pairwise_distances(train_data_matrix,metric='cosine')\n",
    "movie_similarity= pairwise_distances(train_data_matrix.T,meric='cosine')\n",
    "mean_user_rating= train_data_matrix.mean(axis=1)[:,np.newaxis]\n",
    "ratings_diff= (train_data_matrix -mean_user_rating)\n",
    "user_pred= mean_user_rating + user.similarity.dot(ratings_diff)/np.array([np.abs(user_similarity).sum(axis=1)]).T\n",
    "user_pred"
   ]
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
