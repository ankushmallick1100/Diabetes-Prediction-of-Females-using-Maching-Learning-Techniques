import numpy as np
import pickle
import streamlit as st
import warnings 
warnings.simplefilter('ignore')


# Load the saved model
loaded_model = pickle.load(open("C:/Users/ankus/Downloads/Data Science - Project-Internship Purpose/Paper - 2/Diabetes Prediction Using Machine Learning/trained_model.sav", "rb"))

# Creating a function for prediction
def diabetes_prediction(input_data):

    # Changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshaping the array as we are predicting for one instance
    input_data_reshape = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshape)
    # print(prediction)

    if(prediction[0]==0):
        return "The person is not diabetic"
    else:
        return "The person is diabetic"
    

def main():

    # Giving a title
    st.title("Diabetes Prediction Web App")

    # Getting the input datat from the user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glocose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age =  st.text_input('Age of the Person')

    if Pregnancies != "":
        Pregnancies = int(Pregnancies)
    if Glucose != "":
        Glucose = int(Glucose)
    if BloodPressure != "":
      BloodPressure = int(BloodPressure)
    if SkinThickness != "":
        SkinThickness = int(SkinThickness)
    if Insulin != "":
        Insulin = int(Insulin)
    if BMI != "":
        BMI = float(BMI)
    if DiabetesPedigreeFunction != "":
        DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
    if Age != "":
        Age = int(Age)

    # Code for Prediction
    diagnosis = ''

    # Creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])

    st.success(diagnosis)


if __name__ == '__main__':
    main()
