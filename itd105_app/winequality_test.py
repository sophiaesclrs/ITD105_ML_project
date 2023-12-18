from django.shortcuts import render
import pickle

# Load the saved Random Forest model
with open('C:/xampp/htdocs/itd105_ml_algo/itd105_app/MLmodels/wine_model.pkl', 'rb') as file:
    wine_model = pickle.load(file)

wineDict = {0: "Sorry, but some of your suggested parameters are not fit to make a fine wine product. Please do consider necessary adjustments.", 
            1: "Nicely done! All of your suggested parameters are well-balanced for making a fine wine product."}

def text_lowercase(text):
 return text.lower()

def evalWine(request):
    # Get the text
    faText = request.GET.get('fixed_acidity', 'default')
    vaText = request.GET.get('volatile_acidity', 'default')
    caText = request.GET.get('citric_acid', 'default')
    rsText = request.GET.get('residual_sugar', 'default')
    chlText = request.GET.get('chlorides', 'default')
    fsdText = request.GET.get('f_sulfur_dioxide', 'default')
    sdText = request.GET.get('sulfur_dioxide', 'default')
    denText = request.GET.get('density', 'default')
    phText = request.GET.get('pH', 'default')
    sulText = request.GET.get('sulphates', 'default')
    alcText = request.GET.get('alcohol', 'default')
    
    fixed_acidity = float(faText)
    volatile_acidity = float(vaText)
    citric_acid = float(caText)
    residual_sugar = float(rsText)
    chlorides = float(chlText)
    f_sulfur_dioxide = float(fsdText)
    sulfur_dioxide = float(sdText)
    density = float(denText)
    pH = float(phText)
    sulphates = float(sulText)
    alcohol = float(alcText)
    
    wineTest = [[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, 
                chlorides, f_sulfur_dioxide, sulfur_dioxide, density,
                pH, sulphates, alcohol]]
    
    predicted = wine_model.predict(wineTest)
    predicted = wineDict[predicted[0]]
    params = {'wineQual': predicted}
    return render(request, 'itd105_app/predict/wine_result.html', params)
