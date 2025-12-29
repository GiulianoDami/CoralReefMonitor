import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

class CoralReefMonitor:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.train_model()

    def preprocess_data(self):
        X = self.data.drop(['coral_health'], axis=1)
        y = self.data['coral_health']
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self):
        X_train, X_test, y_train, y_test = self.preprocess_data()
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        print(f"Model Accuracy: {accuracy_score(y_test, predictions)}")

    def predict_health(self, temperature, location=None, coral_type=None):
        input_data = {'temperature': [temperature]}
        if location:
            input_data['location'] = [location]
        if coral_type:
            input_data['coral_type'] = [coral_type]
        input_df = pd.DataFrame(input_data)
        prediction = self.model.predict(input_df)
        return prediction[0]