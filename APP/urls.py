from django.urls import path
from knox import views as knox_views
from . import views
from django.urls import path

urlpatterns = [
    path('user/', views.get_user),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('child_add/', views.ADD_CHILD),
    path('child_mdata/', views.ADD_mDATA),
    path('child_adata/', views.ADD_aDATA),
    path('children/',views.get_child),
    path('children/<int:User_id>',views.get_child,name='children'),
    path('getdata/<int:child_id>',views.get_data,name='getdata'),
    path('kpi/<int:kpi_id>',views.get_kpi,name='kpi')

]