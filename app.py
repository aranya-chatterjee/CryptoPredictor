import streamlit as st
import pandas as pd
import numpy as np

# Sample data for cryptocurrency prices
# In a real-world application, you'd fetch this data from a live API
prices = {"Bitcoin": [40000, 41000, 42000], "Ethereum": [2500, 2600, 2700]}
df = pd.DataFrame(prices)

st.title('Cryptocurrency Price Prediction')

# Sidebar for user inputs
st.sidebar.header('User Input Features')
selected_coin = st.sidebar.selectbox('Select Cryptocurrency', df.columns)

# Display the selected cryptocurrency price history
st.subheader(f'Price History of {selected_coin}')
st.line_chart(df[selected_coin])

# Dummy prediction logic
st.subheader('Prediction')
if st.button('Predict'):
    prediction = np.random.randint(30000, 50000)  # Random prediction
    st.success(f'The predicted price for {selected_coin} is ${prediction}')
