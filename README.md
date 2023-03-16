# Comparing Text Classification algorithms

This repository is made for quick (basic) testing of different classifiers.

Classifiers:
  1. Naive Bayes
  2. Logistic Regression
  3. Suport Vector Machine
  
 Dataset used is ecommerceDataset from Kaggle: 
 https://www.kaggle.com/datasets/saurabhshahane/ecommerce-text-classification?resource=download
 
 Classification based E-commerce text dataset for 4 categories - "Electronics", "Household", "Books" and "Clothing & Accessories"
 
 # How to use:
    1. Create conda environment from environment.yml file or make python venv from requirements.txt
    2. load dataset with data_loader.py
    3. run linear_svc.py 
    4. run logistic_regression.py
    5. run naive_bayes.py
   
 # Preprocessing
 
 Preprocessing is done in data_loader.py  
 Using pandas library data is loaded and prepared for processing. Minimal processing was made to assure that classes are balanced.
 Using sklearn library data is transformed into vectors that will be used to train and test classifications models.
 It is possible to load any other labeled dataset with minimal changes in first 5 lines on dataFrame_to_vectors() function.

  # Visualization
  
  Function plot_conusion_matrix() in visualization.py is used to plot confusiuon matrix for all algorithms that are tested.
 
 # Naive Bayes
 
 Algorithm was measured for accuracy and scored: 95%
 
 
 Confusion matrix shows the number of correct and incorrect predictions summarized with count values and broken down by each class

 ![naive_bayes](https://user-images.githubusercontent.com/84984358/224565231-1a643f5d-a886-4321-ad00-1692633105c7.png)
 

 # Logistic Regression
 
 Algorithm was measured for accuracy and scored: 97%
 
 
 Confusion matrix shows the number of correct and incorrect predictions summarized with count values and broken down by each class
 
 ![logerg](https://user-images.githubusercontent.com/84984358/224565838-69b3a9d9-c68f-475f-9d7e-379a6058d11b.png)

 
  # Suport Vector Machine
 
 Algorithm was measured for accuracy and scored: 98%
 
 
 Confusion matrix shows the number of correct and incorrect predictions summarized with count values and broken down by each class
 
 ![svc](https://user-images.githubusercontent.com/84984358/224565919-917fd1f0-0c06-42ce-a190-3f30acc8a8bf.png)


This repo could be extended with other algorithms for testing or could be used to test different parameters of classifiers or both.


 
