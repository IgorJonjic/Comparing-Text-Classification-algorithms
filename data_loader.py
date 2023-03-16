import numpy as np
import pandas as pd
import sklearn
import string
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import _stop_words
from sklearn.model_selection import train_test_split
import itertools


data = pd.read_csv('ecommerceDataset.csv', names=["Label", "Text"])

def dataFrame_to_vectors(data: pd.DataFrame):
    """ Function takes pandas DataFrame and returns train and test vectors for classifiers.
         """
    house_data = data[data['Label'] == 'Household']
    house_data = house_data.drop(house_data.index[:9000])
    data = data.drop(data[data['Label'] == 'Household'].index)
    data = pd.concat([data, house_data])
    data['Label'] = data.Label.map({'Books':1, 'Electronics':2, 'Household':3, 'Clothing & Accessories':4})
    X = data.Text
    y = data.Label
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    vect = CountVectorizer()
    X_train_dtm = vect.fit_transform(X_train)
    X_test_dtm = vect.transform(X_test.astype('U'))
    
    return X_train_dtm, X_test_dtm, y_train, y_test


