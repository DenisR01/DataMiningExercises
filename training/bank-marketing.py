import pandas as pd
from sklearn.tree import export_text
from sklearn import tree
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('bank.csv',encoding = 'utf-8', sep=";")

# print(data.head())
# print(data['y'].value_counts())

data.y.replace(('yes', 'no'), (1, 0), inplace=True)
data.default.replace(('yes','no'),(1,0),inplace=True)
data.housing.replace(('yes','no'),(1,0),inplace=True)
data.loan.replace(('yes','no'),(1,0),inplace=True)
data.marital.replace(('married','single','divorced'),(1,2,3),inplace=True)
data.contact.replace(('telephone','cellular','unknown'),(1,2,3),inplace=True)
data.month.replace(('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'),(1,2,3,4,5,6,7,8,9,10,11,12),inplace=True)
data.education.replace(('primary','secondary','tertiary','unknown'),(1,2,3,4),inplace=True)

# print(data.head())

features_labels = ['housing', 'loan', 'marital', 'contact', 'month', 'education']
X = data[features_labels]
y = data['y']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, shuffle=True)

#DECISION TREE

tr = tree.DecisionTreeClassifier(max_depth=5, criterion='entropy', random_state=42)

# Train
tr.fit(X_train, y_train)

# Afisare tree
r = export_text(tr, feature_names=X.columns.tolist())
print(r)

# Predictii
tr_pred = tr.predict(X_test)

# Confusion matrix
print(confusion_matrix(y_test, tr_pred))#matricea 2pe2

# Classification report
print(classification_report(y_test, tr_pred))

print('Accuracy: %.3f' % tr.score(X_test, y_test))


plt.figure()
plot_tree(tr, filled=True)
plt.show()


