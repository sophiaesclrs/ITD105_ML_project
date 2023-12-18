from django.shortcuts import render
import pickle
import numpy as np

with open('C:/xampp/htdocs/itd105_ml_algo/itd105_app/MLmodels/med_model.pkl', 'rb') as file:
    med_model = pickle.load(file)
    

def evalMed(request):
    # Get the text
    ageText = request.GET.get('age', 'default')
    sexText = request.GET.get('sex', 'default')
    bmiText = request.GET.get('bmi', 'default')
    chiText = request.GET.get('children', 'default')
    smoText = request.GET.get('smoker', 'default')
    regText = request.GET.get('region', 'default')
    
    age = int(ageText)
    sex = int(sexText)
    bmi = float(bmiText)
    children = float(chiText)
    smoker = float(smoText)
    region = float(regText)
    
    medInput = [[age, sex, bmi, children, smoker, region]]
    
    medInput_as_numpy_array = np.asarray(medInput)
    medInput_reshaped = medInput_as_numpy_array.reshape(1, -1)
    prediction = med_model.predict(medInput_reshaped)[0]
    prediction = round(prediction, 2)
    
    params = {'medCost': prediction}
    return render(request, 'itd105_app/predict/med_result.html', params)
