from django.urls import path
from . import views

urlpatterns = [
    # path('about', views.aboutPage, name='about'),
    path('', views.index, name="index"),
    path('list/', views.viewlist, name="view_list"),
]
