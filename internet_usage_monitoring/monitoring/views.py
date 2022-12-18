from django.shortcuts import render
from django.http import HttpResponse
from .models import Monitoring
import csv
import os
from rest_framework import viewsets
from django.core import serializers
from django.http import JsonResponse


def valuescsv():
    path = os.getcwd() + "/monitoring/user_internet.csv"
    print(path)
    tab = []
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print(row)
            m = Monitoring(
                    username=row['username'],
                    mac_adresse=row[' mac_address'],
                    start_time=row[' start_time'],
                    usage_time=row[' usage_time'],
                    upload=row[' upload'],
                    download=row[' download'],
                    )
            m.save()
            print("sauvegader")

        
# Create your views here.
def initialisation_db(request):
    m = len(Monitoring.objects.all())
    
    if m == 0:
        valuescsv()
        return HttpResponse('base de données Initialisé')
    else:
        return HttpResponse('db ok')

def moni(request):
    data = {"status": "ok", "data": []}
    tab = []
    for loop in Monitoring.objects.all().values():
        data["data"].append(loop)
   
    
    return JsonResponse(data)