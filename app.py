import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import time

# Function to preprocess the input data
def preprocess_data(df):
    scaler = MinMaxScaler()
    df['DATE'] = pd.to_datetime(df['DATE'])  # Convert 'DATE' column to datetime
    df['CLOSE'] = scaler.fit_transform(df[['CLOSE']].values)
    return df, scaler

# Function to make predictions using Linear Regression
def make_predictions(df, selected_date):
    df['DATE'] = pd.to_datetime(df['DATE'])  # Ensure 'DATE' column is in datetime format

    df_train = df[df['DATE'] < pd.Timestamp(selected_date)]
    df_test = df[df['DATE'] == pd.Timestamp(selected_date)]

    if len(df_train) < 2:
        return None, None, None

    X_train = np.array(df_train.index).reshape(-1, 1)
    y_train = np.array(df_train['CLOSE'])

    X_test = np.array(df_test.index).reshape(-1, 1)

    # Fit a Linear Regression model
    model = LinearRegression()
    start_time = time.time()
    model.fit(X_train, y_train)
    end_time = time.time()

    # Make predictions
    prediction = model.predict(X_test)
    
    # Calculate MAE score
    mae_score = mean_absolute_error(y_train, model.predict(X_train))

    return prediction, mae_score, end_time - start_time


# Streamlit App
def main():
    st.title("Stock Price Prediction App")

    # Load the data
    df = pd.read_csv('GIAA.csv')

    # Preprocess the data
    df, scaler = preprocess_data(df)

    # Set default date within the allowed range
    default_date = pd.to_datetime('2023-08-15')

    # Allow user to select a date
    selected_date = st.sidebar.date_input('Select a date', min_value=df['DATE'].min(), max_value=df['DATE'].max(), value=default_date)

    # Make predictions for the selected date
    prediction, mae_score, execution_time = make_predictions(df, selected_date)

    # Display the predictions
    if prediction is not None:
        predicted_price = scaler.inverse_transform(prediction.reshape(-1, 1))[0][0]
        st.write(f"Prediction for {selected_date}: {predicted_price}")
        st.write(f"MAE Score: {mae_score}")
        st.write(f"Execution Time: {execution_time} seconds")
    else:
        st.write("Not enough historical data for prediction.")

if __name__ == '__main__':
    main()
