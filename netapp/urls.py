
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'), ##landing dashboard,it hasa view for all tx NEs
    #path('userauth',views.userAuth,name='userauth'),
    path('login/',views.userLogin,name='login'),
    path('logout/',views.userLogout,name='logout'), #url for user to logout
    path('pes/',views.pes,name='pes'),#url for user to view a list PEs
    path('pe/',views.pe,name='pe'), ##example link
    path('nerecord/<int:pk>',views.ne_record,name='nerecord'),#url og viewing details of a sinle NE
    path('add_ne',views.add_ne,name='add_ne'), #url to add ne
    path('delete_ne/<int:pk>',views.delete_nerecord,name='delete_ne'),#url to delete NE
    path('update_ne/<int:pk>',views.update_nerecord,name='update_ne'), #url to update NE
    path('add_pe',views.add_pe,name='add_pe'),#url to add a PE
    path('update_pe/<int:pk>',views.update_pe,name='update_pe'),##a ur to update PE details
    path('delete_pe/<int:pk>',views.delete_pe,name='delete_pe'),##a url to delete PE details
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) ##static route to where statis files as served


