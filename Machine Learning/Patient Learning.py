import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

patient_data = pd.read_csv("C:\\Users\\Ryan\\Documents\\External projects\\Python\\Machine Learning\\Datasets\\patients.csv")
#Get the dataset and split it where commas are
features = patient_data.iloc[:,0:3].values
print(features)
#get the coloumns 0-2 and assign them to features
labels = patient_data.iloc[:,3].values
print(labels)
#Get coloumn 3 and assign it to labels 
imputer = Imputer(missing_values="NaN" , strategy="mean", axis=0)
#any cells with missing values should be filled in with the mean of that coloumns values
imputer = imputer.fit(features[:,1:2])
#find missing values
features[:,1:2] = imputer.transform(features[:,1:2])
#assign the values the mean 
labelencoder_features = LabelEncoder()
#create a label encoder
features[:,2] = labelencoder_features.fit_transform(features[:,2])
#Get the values in coloumn 2 and convert them from catagories to numbers
print(features)
labels = labelencoder_features.fit_transform(labels)
#Get the values in labels and convert them from catagories to numbers
print(labels)
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.25, random_state=0)
#split features and labels into test and train groups
feature_scaler = StandardScaler()
#create a scaler to change numbers onto a smaller scale (close to 1 and -1) as to not have larger numbers dominate te smaller numbers
train_features = feature_scaler.fit_transform(train_features)
#change train features to new scale
test_features = feature_scaler.fit_transform(test_features)
#change test features to new scale
#labels dont need to be changed as they are already 0 or 1
print(train_features)
print(test_features)
