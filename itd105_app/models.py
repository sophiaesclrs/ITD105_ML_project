from django.db import models

class Wine(models.Model):
    fixed_acidity = models.DecimalField(max_digits=3, decimal_places=1)
    volatile_acidity = models.DecimalField(max_digits=5, decimal_places=3)
    citric_acid = models.DecimalField(max_digits=5, decimal_places=3)
    residual_sugar = models.DecimalField(max_digits=5, decimal_places=3)
    chlorides = models.DecimalField(max_digits=5, decimal_places=3)
    f_sulfur_dioxide = models.PositiveIntegerField()
    sulfur_dioxide = models.PositiveIntegerField()
    density = models.DecimalField(max_digits=6, decimal_places=4)
    pH = models.DecimalField(max_digits=3, decimal_places=2)
    sulphates = models.DecimalField(max_digits=3, decimal_places=2)
    alcohol = models.DecimalField(max_digits=4, decimal_places=2)
    quality = models.PositiveIntegerField()
    
    class Meta:
        db_table = "wine_dataset"
        

class Med(models.Model):
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=50)
    bmi = models.DecimalField(max_digits=5, decimal_places=3)
    children = models.PositiveIntegerField()
    smoker = models.CharField(max_length=20)
    region = models.CharField(max_length=100)
    charges = models.DecimalField(max_digits=7, decimal_places=3)
    
    class Meta:
        db_table = "med_dataset"
