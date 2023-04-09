
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    #path('',views.userAuth,name='userauth'),
    path('login/',views.userLogin,name='login'),
    path('logout/',views.userLogout,name='logout'),

]