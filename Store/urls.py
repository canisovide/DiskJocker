from django.urls import path, re_path
from . import views
app_name = "Store"
urlpatterns = [
    path('', views.index, name="hello"),
    path('listing', views.listing, name="listing"),
    re_path(r'^search/$', views.search, name="search"),
    path('disque/', views.details, name="detail")
]
