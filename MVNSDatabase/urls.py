from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='MVNS-index'),
    # path('login/', views.login, name='MVNS-login'),
    path('view/', views.view, name='MVNS-view'),
    path('search_data/', views.search_data, name='MVNS-search-data'),
    path('found_data/<int:pk>/', views.found_data, name='MVNS-found-data'),
    path('add_data/', views.add_data, name='MVNS-add-data'),
    path('edit_data/<int:pk>/', views.edit_data, name='MVNS-edit-data'),
]
