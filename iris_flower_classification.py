# -*- coding: utf-8 -*-
"""IRIS FLOWER - CLASSIFICATION.ipynb


"""### Knowing about the Dataset

**Importing the Required Libraries**
"""

# Pandas Library for Dataframe
import pandas as pd

# Numpy Library for Numerical Calculations
import numpy as np

# Matplotlib and Seaborn for Plottings
import matplotlib.pyplot as plt
import seaborn as sns

# Pickle Library for Saving the Model
import pickle

# Train_Test_Split for splitting the Dataset
from sklearn.model_selection import train_test_split

# KFold and Cross_Val_Score for Validation
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

# Logistic Regression, Decision Tree, K Neighbors, Naive Bayes, SVC and Linear Discriminant are Models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Accuracy Score, Classification Report and Confusion Matrix is for Analysis of Models
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

"""**Reading informations in the Dataset**"""

iris = pd.read_csv("/content/drive/MyDrive/Oasis Infobyte/Data Science - Internship/Iris.csv")

"""**Checking for null values in Data**"""

iris.isnull().sum()

"""**Checking the First Five Values in the Data**"""

iris.head()

"""**Checking the Last Five Values in the Data**"""

iris.tail()

"""**Dropping the unused Column in the Dataset**

In ML, we will not be using the unique identifiers so we are reoving that column
"""

iris = iris.drop(['Id'], axis=1)
iris.columns

"""**Dimensions of the Dataset**"""

iris.shape

"""**Describing the Dataset**"""

print(iris.describe())

"""**Checking for the classes in the Data**"""

print(iris.groupby('Species').size())

"""### Visualization of the Data

**Classes distribution over Count of each class Plotting**
"""

species_plot = iris['Species'].value_counts().plot.bar(title = 'Flower Class Distribution')
species_plot.set_xlabel('Class',size=20)
species_plot.set_ylabel('Count',size=20)

"""Each class has equal distribution

**Box and Whisker Plot**
"""

iris.plot(kind = 'box', subplots = True, layout = (2, 2), 
               sharex = False, sharey = False, title = "Box and Whisker plot for each Attribute")
plt.show()

"""To check the Attribute Distribution

**Histogram Plotting**
"""

iris.hist()
plt.show()

"""To check Value Distribution in the Dataset

**Multivariate Scatter Plot**
"""

sns.set(style = "ticks")
sns.pairplot(iris, hue = "Species")

"""Pair-wise Relationship in Dataset

### Data Modeling

**Splitting the Dataset into Training and Testing**
"""

X = iris.drop(['Species'], axis=1)
Y = iris['Species']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=25)

"""**Checking the Dimensions of Training and Testing Data**"""

print("X_Train Shape:", X_train.shape)
print("X_Test Shape:", X_test.shape)
print("Y_Train Shape:", X_train.shape)
print("Y_Test Shape:", Y_test.shape)

"""### Model Building

**Creating the Models**
"""

# All the Models will be stored in this models list.
models = []

# Linear Models
models.append(('LR', LogisticRegression(solver = 'liblinear', multi_class = "auto")))
models.append(('LDA', LinearDiscriminantAnalysis()))

# Non-linear Models
models.append(('CART', DecisionTreeClassifier()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('GNB', GaussianNB()))
models.append(('SVC', SVC(gamma = "auto")))

print("Model Accuracy")

# Evaluating each Models
names = []
accuracy = []
for name, model in models:
    
    # 15 Cross Fold Validation for each Models
    kfold = KFold(n_splits=15)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    
    # Displaying the Accuracy of each Model in Validation
    names.append(name)
    accuracy.append(cv_results)
    msg = "%s: Accuracy = %f" % (name, cv_results.mean())
    print(msg)

"""### Testing Model

**Testing Models**
"""

models = []

# Linear Models
models.append(('LR', LogisticRegression(solver = 'liblinear', multi_class = "auto")))
models.append(('LDA', LinearDiscriminantAnalysis()))

# Non-linear Models
models.append(('CART', DecisionTreeClassifier()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('GNB', GaussianNB()))
models.append(('SVC', SVC(gamma = "auto")))

"""**Creating Function for Testing the Models**"""

def test_model(model):
    # Training the Dataset with Training Set
    model.fit(X_train, Y_train)
    
    # Predicting the Values with Testing Set
    predictions = model.predict(X_test)
    
    # Model Testing Results
    print("Accuracy:", accuracy_score(Y_test, predictions))
    print("Confusion Matrix:")
    print(confusion_matrix(Y_test, predictions))
    print("Classification Report:")
    print(classification_report(Y_test, predictions))

"""**Testing the Models**"""

# Predicting the Values
for name, model in models:
    print("----------------")
    print("Testing:", name)
    test_model(model)

"""In Testing Top 3 Models are,

1.   SVC
2.   CART
3.   LDA

### Saving Models

**Saving the Best Performed Models**
"""

for name, model in models:
    filename = name + ".pkl"
    pickle.dump(model, open(filename, 'wb'))
print("Saved all Models")
