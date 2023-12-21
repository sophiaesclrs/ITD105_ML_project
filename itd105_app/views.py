from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from itd105_app.models import Wine
from itd105_app.models import Med

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('/signup')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'itd105_app/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'itd105_app/signup.html', {'form': form})

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/main')
        else:
            msg = 'Incorrect credentials. Please try again.'
            form = AuthenticationForm(request.POST)
            return render(request, 'itd105_app/index.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'itd105_app/index.html', {'form': form})

def dashboard(request):
    return render(request, 'itd105_app/dashboard.html')

def wine(request):
    
    # fetching data from db
    wine_report = Wine.objects.all().values()
    
    # Fetch the specific data
    wine_data = Wine.objects.all().count()
    wine1 = Wine.objects.filter(quality=3).count()
    wine2 = Wine.objects.filter(quality=4).count()
    wine3 = Wine.objects.filter(quality=5).count()
    wine4 = Wine.objects.filter(quality=6).count()
    wine5 = Wine.objects.filter(quality=7).count()
    wine6 = Wine.objects.filter(quality=8).count()
    
    wine1 = int(wine1)
    wine2 = int(wine2)
    wine3 = int(wine3)
    wine4 = int(wine4)
    wine5 = int(wine5)
    wine6 = int(wine6)
    
    # wine quality: bar graph
    bad_wine = wine1 + wine2 + wine3 + wine4
    good_wine = wine5 + wine6
    
    wine_bins = [3, 4, 5, 6, 7, 8]
    wine_lists = [wine1, wine2, wine3, wine4, wine5, wine6]
    
    
    
    
 
    context = {
        'wine_report': wine_report,
        'wine_data': wine_data,
        'good_wine': good_wine,
        'bad_wine': bad_wine,
        'wine_bins': wine_bins,
        'wine_lists': wine_lists
    }
    
    return render(request, 'itd105_app/wine.html', context)


def wine_predict(request):            
    return render(request, 'itd105_app/predict/wine_predict.html')

def med(request):
    
    # fetching data from db
    med_report = Med.objects.all()
    
    # Fetch the specific data
    med_data = Med.objects.all().count()
    no_child = Med.objects.filter(children=0).count()
    one_child = Med.objects.filter(children=1).count()
    two_child = Med.objects.filter(children=2).count()
    three_child = Med.objects.filter(children=3).count()
    four_child = Med.objects.filter(children=4).count()
    five_child = Med.objects.filter(children=5).count()
    
    one_child = int(one_child)
    two_child = int(two_child)
    three_child = int(three_child)
    four_child = int(four_child)
    five_child = int(five_child)
    
    has_child = one_child + two_child + three_child + four_child + five_child
    
    context = {
        'med_report': med_report,
        'med_data': med_data,
        'no_child': no_child,
        'has_child': has_child
    }
    
    return render(request, 'itd105_app/med.html', context)

def med_predict(request):
    return render(request, 'itd105_app/predict/med_predict.html')


def signout(request):
    logout(request)
    return redirect('/')
