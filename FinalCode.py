Original file is located at
    https://colab.research.google.com/drive/18Cadhk8tsoSl-mDCNs59UqCXX_Hldg48
"""

import pandas as pd

df= pd.read_csv('Stock_Dataa.csv',encoding='ISO-8859-1')

# LOOKING AT TOP 5 RECORDS OF DATASET
df.head()

# LOOKING AT LAST 5 RECORDS OF THE DATASET
df.tail()

# DIVIDING THE DATASET INTO TRAINING AND TEST SETS ACCORDING TO DATE
train= df[df['Date']< '20150101' ]
test=  df[df['Date']> '20141231']

# REMOVING PUNCTUATIONS
data= train.iloc[:,2:27]
data.replace("[^a-zA-Z]"," ",regex=True, inplace=True)

# RENAMING COLUMN NAME FOR EASE OF ACCESS
list1=[i for i in range(25)]
new_Index=[str(i) for i in list1]
data.columns= new_Index
data.head()

# CONVERTING THE HEADLINES INTO LOWER CASE
for index in new_Index:
    data[index]=data[index].str.lower()
data.head(1)

# COMBINING THE TOP 25 HEADLINES OF 1ST RECORD
' '.join(str(x) for x in data.iloc[1,0:25])

# COMBINING THE TOP 25 HEADLINES FOR EACH RECORD IN THE DATASET SO THAT WE COULD CONVER THEM INTO VECTORS
headlines=[]
for row in range(0,len(data.index)):
    headlines.append(' '.join(str(x) for x in data.iloc[row,0:25]))

# EXAMPLE- COMBINED ALL THE HEADLINES OF 0th RECORD
headlines[0]

# Count vectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

## IMPLEMENTING BAG OF WORDS MODEL
countvector= CountVectorizer(ngram_range=(2,2))
traindataset= countvector.fit_transform(headlines) # CONVERTING ALL THE HEADLINES INTO VECTORS

# DATA CONVERTS INTO SPARSE MATRIX
traindataset[0]

# Implement RandomForestClassifier on traindataset
random_classifier= RandomForestClassifier(n_estimators=200,criterion='entropy')
random_classifier.fit(traindataset,train['Label'])

## PREDICTING FOR TEST DATASET
# WE WILL BE PERFORMING SAME STEPS FOR TEST DATA ALSO.

test_transform=[]
for row in range(0,len(test.index)):
    test_transform.append(' '.join(str(x) for x in test.iloc[row,2:27]))
test_dataset= countvector.transform(test_transform)
predictions= random_classifier.predict(test_dataset)

# LOOKING AT OUR PREDICTIONS
predictions

# FOR CHECKING ACCURACY
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report

matrix= confusion_matrix(test["Label"],predictions)
print(matrix)
score= accuracy_score(test["Label"],predictions)
print(score)
report= classification_report(test['Label'],predictions)
print(report)

# USING RANDOM FOREST CLASSIFIER WITH TF-IDF VECTORIZER
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

## IMPLEMENTING TF-IDF VECTORIZER
tfidf= TfidfVectorizer(ngram_range=(2,2))
traindataset= tfidf.fit_transform(headlines) # CONVERTING ALL THE HEADLINES INTO VECTORS using TF-IDF technique

# Implement RandomForestClassifier on traindataset
random_classifier= RandomForestClassifier(n_estimators=200,criterion='entropy')
random_classifier.fit(traindataset,train['Label'])

## PREDICTING FOR TEST DATASET
# WE WILL BE PERFORMING SAME STEPS FOR TEST DATA ALSO.

test_transform=[]
for row in range(0,len(test.index)):
    test_transform.append(' '.join(str(x) for x in test.iloc[row,2:27]))
test_dataset= tfidf.transform(test_transform)
predictions= random_classifier.predict(test_dataset)

# ACCURACY AFTER USING TF-IDF VECTORIZER
matrix= confusion_matrix(test["Label"],predictions)
print(matrix)
score= accuracy_score(test["Label"],predictions)
print(score)
report= classification_report(test['Label'],predictions)
print(report)

from sklearn.naive_bayes import MultinomialNB
naive= MultinomialNB()

# WE WILL FIRST USE BAG OF WORDS MODEL FOR CONVERTING TEXT INTO VECTORS
## IMPLEMENTING BAG OF WORDS MODEL
countvector= CountVectorizer(ngram_range=(2,2))
traindataset= countvector.fit_transform(headlines) # CONVERTING ALL THE HEADLINES INTO VECTOR

# FITTING TRAIN DATA INTO  NAIVE BAYES CLASSIFIER
naive.fit(traindataset,train['Label'])

## PREDICTING FOR TEST DATASET
# WE WILL BE PERFORMING SAME STEPS FOR TEST DATA ALSO.

test_transform=[]
for row in range(0,len(test.index)):
    test_transform.append(' '.join(str(x) for x in test.iloc[row,2:27]))
test_dataset= countvector.transform(test_transform)
predictions= naive.predict(test_dataset)

# LOOKING AT OUR PREDICTIONS
predictions

# FOR CHECKING ACCURACY
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report

matrix= confusion_matrix(test["Label"],predictions)
print(matrix)
score= accuracy_score(test["Label"],predictions)
print(score)
report= classification_report(test['Label'],predictions)
print(report)

# NOW WE WILL USE TF-IDF VECTORIZER WITH NAIVE BAYES CLASSIFIER
traindataset= tfidf.fit_transform(headlines) # CONVERTING ALL THE HEADLINES INTO VECTORS using TF-IDF technique

naive.fit(traindataset,train['Label'])

## PREDICTING FOR TEST DATASET
# WE WILL BE PERFORMING SAME STEPS FOR TEST DATA ALSO.

test_transform=[]
for row in range(0,len(test.index)):
    test_transform.append(' '.join(str(x) for x in test.iloc[row,2:27]))
test_dataset= countvector.transform(test_transform)
predictions= naive.predict(test_dataset)

predictions

# ACCURACY AFTER USING TF-IDF VECTORIZER IN NAIVE BAYES CLASSIFIER
matrix= confusion_matrix(test["Label"],predictions)
print(matrix)
score= accuracy_score(test["Label"],predictions)
print(score)
report= classification_report(test['Label'],predictions)
print(report)

