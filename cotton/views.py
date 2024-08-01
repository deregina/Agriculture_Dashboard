from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import *

import os
import pandas as pd
import geopandas as gpd
import geemap
from .forms import *


def home(request):
	data = Cc2019.objects.all()
	
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Logged In")
			return redirect('home')
		else:
			messages.success(request, "Username or Password Error")
			return redirect('home')
	else:
		return render(request, 'home.html')

def logout_user(request):
	logout(request)
	messages.success(request, "Logged Out")
	return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Registered. Please Log in.")
            return redirect('home')
    
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})


# Tables and Graphs

feature_list = ['CC', 'PH', 'CV', 'ExG', 'yield']

year_list = ['2019', '2020', '2021', '2022', '2023']

model_dict = {'Cc2019':Cc2019, 'Cc2020':Cc2020, 'Cc2021':Cc2021, 'Cc2022':Cc2022, 'Cc2023':Cc2023,
              'Cv2019':Cv2019, 'Cv2020':Cv2020, 'Cv2021':Cv2021, 'Cv2022':Cv2022, 'Cv2023':Cv2023,
              'Ecv2019':Ecv2019, 'Ecv2020':Ecv2020, 'Ecv2021':Ecv2021, 'Ecv2023':Ecv2023,
              'Exg2019':Exg2019, 'Exg2020':Exg2020, 'Exg2021':Exg2021, 'Exg2022':Exg2022, 'Exg2023':Exg2023,
              'Ph2019':Ph2019, 'Ph2020':Ph2020, 'Ph2021':Ph2021, 'Ph2022':Ph2022, 'Ph2023':Ph2023,
              'Yield2019':Yield2019, 'Yield2020':Yield2020, 'Yield2021':Yield2021, 'Yield2022':Yield2022, 'Yield2023':Yield2023,              
            }

def get_table(request, year_feature):
    if request.user.is_authenticated:
        # Look Up Data
        data = model_dict[year_feature].objects.all()
        return render(request, 'table.html', {'data':data})

    else:
        messages.success(request, "You must be Logged in to View the Page...")
        return redirect('home')

from .utils import *

def get_avg_line(request, year_feature):
    if request.user.is_authenticated:
        # Look Up Data

        data = pd.DataFrame(list(model_dict[year_feature].objects.all().values()))
        cols = list(data.columns)[1:]
        avg = list(data.iloc[:, 1:].mean())

        chart = draw_plot(cols, avg, year_feature)

        return render(request, 'graph.html', {'chart':chart})

    else:
        messages.success(request, "You must be Logged in to view the page")
        return redirect('home')


def get_map(request, year='2022', feature='CC', date='d220408'):
    if request.user.is_authenticated:
        context = {}
        
        data = gpd.read_file(f"cotton/geojson/geodata{year}_{feature}.geojson")
        cols = list(data.columns)[1:-1]
        m = data.explore(column=date, categorical=True, cmap='RdYlGn', legend=False)

        context['map'] = m._repr_html_()

        context['year'] = year
        context['feature'] = feature
        context['date'] = date
        context['index'] = cols.index(date)

        context['data'] = data
        context['year_list'] = year_list
        context['feature_list'] = feature_list
        context['dates'] = cols
    
    
        return render(request, 'base_map.html', context)
    else:
        messages.success(request, "You must be Logged in to View the Page...")
        return redirect('home')

def draw_map(request):
     return render(request, 'make_shp.html')
      
import json

@csrf_exempt
def geojson_to_shp(request):
    if request.method == 'POST':
        geojson_data = json.loads(request.body)
        # Process the geojson data
        print(geojson_data)
        context = {'geojson_data':geojson_data}

        # Respond with a success message
        return render(request, 'download_shp.html', context)
    return JsonResponse({'result': 'error', 'message': 'Invalid request'}, status=400)

    # return render(request, 'graph.html', {'chart':chart})
    # return JsonResponse({'result': 'success'})

