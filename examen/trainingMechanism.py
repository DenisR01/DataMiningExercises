from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score


bank_marketing = fetch_ucirepo(id=222)


X = bank_marketing.data.features
y = bank_marketing.data.targets


y = y.iloc[:, 0]


def preprocess_data(X, y):

    label_encoders = {}
    for column in X.select_dtypes(include=['object']).columns:
        label_encoders[column] = LabelEncoder()
        X.loc[:, column] = label_encoders[column].fit_transform(X[column])

    label_encoder_y = LabelEncoder()
    y = label_encoder_y.fit_transform(y)

    scaler = StandardScaler()
    X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

    return X, y


X, y = preprocess_data(X, y)


def split_data(X, y):
    train_size = int(0.9 * len(X))
    X_train = X[:train_size]
    y_train = y[:train_size]
    X_test = X[train_size:]
    y_test = y[train_size:]

    return X_train, y_train, X_test, y_test


X_train, y_train, X_test, y_test = split_data(X, y)


def train_and_evaluate(X_train, y_train, X_test, y_test):
    model = LogisticRegression(max_iter=2000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))


train_and_evaluate(X_train, y_train, X_test, y_test)
