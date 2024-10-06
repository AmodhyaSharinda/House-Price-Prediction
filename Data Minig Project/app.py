# backend/app.py
from flask import Flask, request, jsonify
import pickle
import pandas as pd
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.compose import ColumnTransformer

app = Flask(__name__)

# Load the trained model
with open('filtered_label_encoders.pkl', 'rb') as file:
    label_encoder = pickle.load(file)

# Load the trained model
with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load preprocessing objects (these should have been saved during training)
with open('new_scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

    
categorical_columns = [
    "KitchenQual",
    "GarageType",
    "GarageFinish",
    "ExteriorQuality_Condition",
    "BasementQuality_Condition"
]

numerical_columns = [
    "LotArea",
    "MasVnrArea",
    "TotRmsAbvGrd",
    "Fireplaces",
    "GarageArea",
    "AgeBuilt",
    "AgeRemod",
    "totalsf",
    "totalarea",
    "totalbaths",
    "OverallQuality_Condition",
]

# Create a function to preprocess the input data
def preprocess_input(input_keys_dict):
    # Convert input_keys_dict to DataFrame
    df = pd.DataFrame([input_keys_dict])  # Wrap in a list to create a DataFrame
    print(df)
    # Fit the numerical transformer on the numerical columns
    df[numerical_columns] = scaler.transform(df[numerical_columns])

    # Encode each categorical column
    for col in categorical_columns:
        if col in df.columns:
            le = label_encoder[col]
            df[col] = le.transform(df[col].astype(str)) 

    # Convert DataFrame back to NumPy array
    # X_preprocessed = df.values.flatten()

    # print("Training features:", X_preprocessed.tolist())
    return df
    # return X_preprocessed.tolist()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get data from the frontend
    print("Received data:", data)
    df = preprocess_input(data)
    # preProcessed = preprocess_input(data)
    # df = pd.DataFrame([preProcessed]) # Convert data to DataFrame format

    print("Received data:", df)

    # Make prediction using the preprocessed data
    prediction = model.predict(df)


    # Convert prediction to a scalar
    predicted_price = float(prediction[0]) if prediction.ndim > 0 else float(prediction)

    return jsonify({'predicted_price': predicted_price})

if __name__ == '__main__':
    app.run(debug=True)
