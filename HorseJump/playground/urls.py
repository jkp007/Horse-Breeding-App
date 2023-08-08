from django.urls import path
from . import views

#URL Conf
urlpatterns = [
    path('', views.homePage),
    path('predictbyname', views.predictByName),
    path('predictbyheight', views.predictByHeight),
    path('aboutus', views.aboutUs),
    path('faq', views.faq),
    path('predict_by_height', views.predict_by_height)
]
