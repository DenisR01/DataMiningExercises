from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# === Încărcare dataset ===
bank_marketing = fetch_ucirepo(id=222)
X = bank_marketing.data.features
y = bank_marketing.data.targets
y = y.iloc[:, 0]

# === Preprocesare ===
def preprocess_data(X, y):
    for column in X.select_dtypes(include=['object']).columns:
        X[column] = LabelEncoder().fit_transform(X[column])
    y = LabelEncoder().fit_transform(y)
    X = pd.DataFrame(StandardScaler().fit_transform(X), columns=X.columns)
    return X, y

X, y = preprocess_data(X, y)

# === Împărțire în train/test ===
def split_data(X, y):
    train_size = int(0.9 * len(X))
    return X[:train_size], y[:train_size], X[train_size:], y[train_size:]

X_train, y_train, X_test, y_test = split_data(X, y)

# === Antrenare, evaluare și salvare ===
def train_and_evaluate(X_train, y_train, X_test, y_test):
    model = LogisticRegression(max_iter=2000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # === Afișare metrici generale ===
    print("📊 Accuracy:", accuracy_score(y_test, y_pred))
    print("\n📋 Classification Report:")
    print(classification_report(y_test, y_pred))

    # === Construire tabel cu rezultate ===
    df_results = X_test.copy()
    df_results['Actual'] = y_test
    df_results['Predicted'] = y_pred

    # === Salvare în CSV ===
    df_results.to_csv('marketing_predictions.csv', index=False)
    print("\n✅ Rezultatele au fost salvate în marketing_predictions.csv")

train_and_evaluate(X_train, y_train, X_test, y_test)