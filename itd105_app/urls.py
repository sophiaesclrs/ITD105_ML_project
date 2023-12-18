from django.urls import path
from . import views
from . import winequality_test
from . import medicalcost_test

urlpatterns = [
    path('', views.index),
    path('main/', views.dashboard, name='category'),
    path('signup/', views.signup),
    
    path('WQT/', views.wine, name='wine'),
    path('WQT/wine_predict', views.wine_predict, name='wine_prediction'),
    path('winePred', winequality_test.evalWine, name='winePred'),
    
    path('MCP/', views.med, name='med'),
    path('MCP/med_predict', views.med_predict, name='med_prediction'),
    path('medPred', medicalcost_test.evalMed, name='medPred'),
    
    path('signout/', views.signout)
]