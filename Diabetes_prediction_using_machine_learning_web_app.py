import numpy as np
import pickle
import streamlit as st
import warnings 
warnings.simplefilter('ignore')


# Load the saved model
loaded_model = pickle.load(open("trained_model.sav", "rb"))

# Creating a function for prediction
def diabetes_prediction(input_data):

    # Changing the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshaping the array as the prediction is done for one instance
    input_data_reshape = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshape)
    # print(prediction)

    if(prediction[0]==0):
        return "The person is not diabetic."
    else:
        return "The person is diabetic."
    

def main():

    # Giving a title
    st.title("Diabetes Prediction System Web App")

    # Getting the input data from the user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glocose Level')
    BloodPressure = st.text_input('Blood Pressure Value - Give a single value')
    SkinThickness = st.text_input('Skin Thickness Value - Give a single value')
    Insulin = st.text_input('Insulin Level - Give a single value')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age =  st.text_input('Age of the person')

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
    if st.button('Please click for getting Diabetes Test Result'):
        if Pregnancies == "" or Glucose == "" or BloodPressure == "" or SkinThickness == "" or Insulin == "" or BMI == "" or DiabetesPedigreeFunction == "" or Age == "":
            st.warning("Please fill all the fields.")
        else:
            diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])

    st.success(diagnosis)


if __name__ == '__main__':
    main()