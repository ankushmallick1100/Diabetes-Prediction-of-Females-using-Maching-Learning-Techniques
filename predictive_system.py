import numpy as np
import pickle
import warnings 
warnings.simplefilter('ignore')

# Load the saved model
loaded_model = pickle.load(open("trained_model.sav", "rb"))

input_data = (6,148,72,35,0,33.6,0.627,50)

# Changing the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshaping the array as the prediction is done for one instance
input_data_reshape = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshape)
print(prediction)

if(prediction[0]==0):
    print("The person is not diabetic.");
else:
    print("The person is diabetic.");