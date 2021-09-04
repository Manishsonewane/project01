from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact, name='contact'),
    path('sendmail',views.sendmail, name='sendmail'),
    path('companys',views.companys, name='companys'),
    path('steel',views.steel, name='steel'),
]