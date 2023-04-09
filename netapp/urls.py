
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    #path('userauth',views.userAuth,name='userauth'),
    path('login/',views.userLogin,name='login'),
    path('logout/',views.userLogout,name='logout'),
    path('pes/',views.pes,name='pes'),

]