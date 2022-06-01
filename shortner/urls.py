
from django.urls import path, include
from shortner import views
#from . import views

urlpatterns = [
    
    path('', views.home_view, name='home'),
    path('<code>/', views.link_redirect, name='link_redirect')
]
    #Add an import:  from my_app import views
    #2. Add a URL to urlpatterns:  path('', views.home, name='home')