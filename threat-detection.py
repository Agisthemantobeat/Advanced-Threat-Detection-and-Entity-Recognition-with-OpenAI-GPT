import pandas as pd
from sklearn.ensemble import IsolationForest
import openai
import os

# Set OpenAI API configurations

# openai.api_type =
# openai.api_base =
# openai.api_version =
# openai.api_key = 


# Load and preprocess data
def load_and_preprocess_data():
    data = pd.read_csv('test.csv')

    # Preprocess data
    data.dropna(inplace=True)

    categorical_cols = ['category1', 'category2', 'category3']
    data = pd.get_dummies(data, columns=categorical_cols)

    numerical_cols = ['numeric1', 'numeric2', 'numeric3']
    data[numerical_cols] = (data[numerical_cols] - data[numerical_cols].mean()) / data[numerical_cols].std()

    feature_cols = ['feature1', 'feature2', 'feature3']
    data[feature_cols] = data[feature_cols] / data[feature_cols].max()

    return data

# Anomaly Detection Model
def train_anomaly_detection_model(X):
    model = IsolationForest(contamination=0.05)  # Adjust parameters accordingly
    model.fit(X)
    return model

# Behavioral Analysis using GPT-3.5
def analyze_behavior(text):
    prompt = f"Summarize the behavior patterns in the given data using a single word: '{text}'"
    response = openai.ChatCompletion.create(
        engine="gpt-35-turbo-16k",
        messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None)
    # print(response)
    behavioral_analysis = response['choices'][0]['message']['content'].strip()
    return behavioral_analysis

# Integration and Decision Making
def detect_threats(anomaly_labels, behavioral_analysis):
    print(anomaly_labels, behavioral_analysis)
    if anomaly_labels == -1 and ("suspicious" in behavioral_analysis or "Exploitable" in behavioral_analysis or "Vulnerability" in behavioral_analysis):
        print("Threat detected!")

    else:
        print("No threat detected.")

# Entry point of the script
if __name__ == "__main__":
    data = load_and_preprocess_data()

    X = data.drop('text', axis=1)  # Features (excluding 'text' column)

    anomaly_model = train_anomaly_detection_model(X)

    anomaly_labels = anomaly_model.predict(X)

    for index, row in data.iterrows():
        behavioral_analysis = analyze_behavior(row['text'])
        detect_threats(anomaly_labels[index], behavioral_analysis)
