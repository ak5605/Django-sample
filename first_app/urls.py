from django.conf.urls import url
from first_app import views

app_name = 'first_app'

urlpatterns = [
    url('register/',views.register,name='register'),
    url('user_login/',views.user_login,name='user_login'),
    url('iser_logout/',views.user_logout,name='user_logout'),



]
