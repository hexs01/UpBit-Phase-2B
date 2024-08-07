import joblib
import streamlit as st

# Load the model
model = joblib.load(r'random_forest_model_v2.joblib')

# Define the prediction function
def prediction(first, second):
    prediction = model.predict([[first, second]])
    performance = ['Low Performance', 'Moderate Performance','Solid Performance','High Performance']
    revenue = ['Low Revenue','Moderate Revenue','Steady Revenue','High Revenue']
    affordability = ['Low Affordability','Limited Affordability','Moderate Affordability','High Affordability']
    return [performance[prediction[0]],revenue[prediction[0]],affordability[prediction[0]]]

# Streamlit interface
st.title("UpBit Affordability Prediction")

# Create sliders for input
capex = st.slider("CAPEX (RM mil)", min_value=0, max_value=150)
opex = st.slider("OPEX (RM mil)", min_value=0, max_value=150)


# Button to make the prediction
if st.button("Predict"):
    result = prediction(capex, opex)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write(f"<div style='font-size:24px;'>Predicted Performance: {result[0]}</div>", unsafe_allow_html=True)
        
    with col2:
        st.write(f"<div style='font-size:24px;'>Predicted Revenue: {result[1]}</div>", unsafe_allow_html=True)
        
    with col3:
        st.write(f"<div style='font-size:24px;'>Predicted Affordability: {result[2]}</div>", unsafe_allow_html=True)
    '''st.write(f"<div style='font-size:24px;'>Predicted Performance: {result[0]}</div>", unsafe_allow_html=True)
    st.write(f"<div style='font-size:24px;'>Predicted Revenue: {result[1]}</div>", unsafe_allow_html=True)
    st.write(f"<div style='font-size:24px;'>Predicted Affordability: {result[2]}</div>", unsafe_allow_html=True)'''