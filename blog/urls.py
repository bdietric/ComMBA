from django.conf.urls import patterns, url
from blog import views

urlpatterns =[

    url(r'^accueil$', views.home),
    url(r'^date$', views.date_actuelle, name='date'),
    url(r'^contact/$',views.contact,name='contact'),
  
]
