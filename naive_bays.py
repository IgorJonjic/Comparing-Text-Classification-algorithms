from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix 
from sklearn import metrics
from data_loader import dataFrame_to_vectors
import pandas as pd
import matplotlib as mpl 
import matplotlib.cm as cm 
import matplotlib.pyplot as plt 
from visualization import plot_confusion_matrix


data = pd.read_csv('ecommerceDataset.csv', names=["Label", "Text"])

X_train_dtm, X_test_dtm, y_train, y_test = dataFrame_to_vectors(data)
naive_bays_model= MultinomialNB()

def train_test_model(X_train, X_test, Y_train, Y_test, model):
    """ Function takes in vectors for training and testing model for classification.
        It prints out accuracy and shows confusion matrix """
    model = model
    model.fit(X_train_dtm, y_train)
    y_pred_class = model.predict(X_test_dtm)
    cnf_matrix = confusion_matrix(y_test, y_pred_class) 
    print("Accuracy: ", accuracy_score(y_test, y_pred_class))
    plt.figure(figsize=(8,6))
    plot_confusion_matrix(cnf_matrix, classes=['Books','Electronics','Household','Clothing & Accessories'],normalize=True,
                        title='Confusion matrix with all features')
    
    
train_test_model( X_train_dtm, X_test_dtm, y_train, y_test, naive_bays_model )    
    

