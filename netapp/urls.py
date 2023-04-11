
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    #path('userauth',views.userAuth,name='userauth'),
    path('login/',views.userLogin,name='login'),
    path('logout/',views.userLogout,name='logout'),
    path('pes/',views.pes,name='pes'),
    path('pe/',views.pe,name='pe'),
    path('nerecord/<int:pk>',views.ne_record,name='nerecord'),
    #path('perecord/<int:pk>',views.pe_record,name='perecord'),
    path('delete_ne/<int:pk>',views.delete_nerecord,name='delete_ne')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


