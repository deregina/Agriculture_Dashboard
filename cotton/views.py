from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
import pandas as pd
import geopandas as gpd


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


# Tables and Graphs

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
        messages.success(request, "You must be Logged in to View the Page...")
        return redirect('home')
    
map_dict = {'2019':Shp2019, '2022':Shp2022}

def get_map(request, year):
    
    data = gpd.read_file("cotton/geojson/geodata2022_CC.geojson")

    #   data = gpd.GeoDataFrame(list( model_dict['Cc'+year].objects.all().values()) )
    #   shp = gpd.GeoDataFrame(list( map_dict[year].objects.all().values()) )

    #   data = data.merge(shp, left_on="fid", right_on="fid")
    #   t = type(data)
      
    m = data.explore(column="d220603", categorical=True, cmap='RdYlGn')

    #   data_col = data.columns
    #   shp_col = shp.columns

    return render(request, 'base_map.html', {'data':data, 'map':m._repr_html_()})  #, 'map':m._repr_html()})