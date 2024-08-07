import joblib
import streamlit as st

# Load the model
model = joblib.load(r'random_forest_model.joblib')

# Define the prediction function
def prediction(first, second, third, forth):
    prediction = model.predict([[first, second, third, forth]])
    label = ['Not Affordable', 'Affordable']
    return label[prediction[0]]

# Streamlit interface
st.title("Affordability Prediction")

# Create sliders for input
capex = st.slider("CAPEX (RM mil)", min_value=0, max_value=1000)
opex = st.slider("OPEX (RM mil)", min_value=0, max_value=1000)
performance = st.slider("Performance", min_value=0, max_value=5)
revenue = st.slider("Revenue (RM mil)", min_value=0, max_value=1000)

# Button to make the prediction
if st.button("Predict"):
    result = prediction(capex, opex, performance, revenue)
    st.write(f"""
        <div style='font-size:24px;'>
            Predicted Affordability:<br>
            <span style='font-size:20px;'>{result[}</span>
        </div>
        """, unsafe_allow_html=True)
