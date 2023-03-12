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
 
 
 Confusion matrix shows the number of correct and incorrect predictions summarized with count values and broken down by each class

 ![naive_bayes](https://user-images.githubusercontent.com/84984358/224565231-1a643f5d-a886-4321-ad00-1692633105c7.png)
 

 # Logistic Regresion
 
 Algorithm was measured for accuracy and scored: 97%
 
 
 Confusion matrix shows the number of correct and incorrect predictions summarized with count values and broken down by each class
 
 ![logerg](https://user-images.githubusercontent.com/84984358/224565838-69b3a9d9-c68f-475f-9d7e-379a6058d11b.png)

 
  # Suport Vector Machine
 
 Algorithm was measured for accuracy and scored: 98%
 
 
 Confusion matrix shows the number of correct and incorrect predictions summarized with count values and broken down by each class
 
 ![svc](https://user-images.githubusercontent.com/84984358/224565919-917fd1f0-0c06-42ce-a190-3f30acc8a8bf.png)



 
