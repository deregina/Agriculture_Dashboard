from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('table/<slug:year_feature>', views.get_table, name='table'),
    path('graph/<slug:year_feature>', views.get_avg_line, name='graph'),
    path('maps/<slug:year>', views.get_map, name='map'),
]