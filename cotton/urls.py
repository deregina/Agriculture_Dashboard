from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('table/<slug:year_feature>', views.get_table, name='table'),
    path('graph/<slug:year_feature>', views.get_avg_line, name='graph'),
    path('maps/<slug:year>/<slug:feature>/<slug:date>', views.get_map, name='map'),
    path('make_shp/', views.draw_map, name='make_shp'),
    path('download_shp/', views.geojson_to_shp, name='geojson_to_shp'),
]