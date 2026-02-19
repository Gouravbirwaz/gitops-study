
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib


def return_model():
    iris = load_iris()
    X = iris.data        # features
    y = iris.target    

    # 2. Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3. Create Random Forest model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

# 4. Train
    model.fit(X_train, y_train)
    joblib.dump(model, "random_forest_iris.pkl")
    return model



if __name__=="__main__":
    predictions = model.predict(X_test)

    # 6. Evaluate
    accuracy = accuracy_score(y_test, predictions)

    print("Accuracy:", accuracy)
    print("\nClassification Report:\n")
    print(classification_report(y_test, predictions))

