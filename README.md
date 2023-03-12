# Comparing-Text-Classification-algorithms

This repository is made for quick (basic) testing of different classifiers.

Classifiers:
  1. Naive Bayes
  2. Logistic Regresion
  3. Suport Vector Machine
  
 Dataset used is ecommerceDataset from Kaggle: 
 https://www.kaggle.com/datasets/saurabhshahane/ecommerce-text-classification?resource=download
 
 Classification based E-commerce text dataset for 4 categories - "Electronics", "Household", "Books" and "Clothing & Accessories"
 
 
 # Preprocessing
 
 Preprocessing done in data_loader.py 
 Using pandas library data is loaded and prepared for processing. Minimal processing was made to assure that classes are balanced.
 Using sklearn library data is transformed into vectors that will be used to train and test classifications models.
 
 
 # Naive Bayes
 
 Algorithm was measured for accuracy and scored: 95%

 ![naive_bayes](https://user-images.githubusercontent.com/84984358/224565231-1a643f5d-a886-4321-ad00-1692633105c7.png)
