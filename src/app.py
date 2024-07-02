import streamlit as st
import numpy as np
import pickle
import os

if os.path.exists('/workspaces/Streamlit-project-fertr/models/multiple_linear_regression.sav'):
    with open('/workspaces/Streamlit-project-fertr/models/multiple_linear_regression.sav', 'rb') as file:
        model = pickle.load(file)


st.title('Medical Charges Predictor')

# Crear entradas de usuario para las características
age = st.slider('Age 🧓', min_value=18, max_value=100, value=25)
bmi = st.slider('BMI ⚖️', min_value=18.0, max_value=40.0, value=25.0)
children = st.number_input('Number of Children 👶', min_value=0, max_value=10, value=0)
sex_n = st.selectbox('Sex 🚻', options=[('Male', 1), ('Female', 0)], format_func=lambda x: x[0])
smoker_n = st.selectbox('Smoker 🚬', options=[('Yes', 0), ('No', 1)], format_func=lambda x: x[0])


# Convertir las opciones de selección a sus valores correspondientes
sex_n = sex_n[1]
smoker_n = smoker_n[1]

# Crear un botón para realizar la predicción
if st.button('Predict'):
    # Crear un array con los valores de las características
    features = np.array([[age, bmi, children, sex_n, smoker_n]])
    
    # Realizar la predicción
    prediction = model.predict(features)
    
    # Mostrar el resultado
    st.write(f'The predicted medical charge is: ${prediction[0]:.2f}')