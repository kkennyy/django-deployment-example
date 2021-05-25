from django.urls import path
from basicapp import views

app_name = 'basicapp'

urlpatterns = [
    path('', views.index,name='index'),
    path('form/', views.profile_form_view,name='profile_form'),
    path('contact/', views.contact,name='contact'),
    path('relative/', views.relative,name='relative'),
    path('register/', views.register,name='register'),
    path('user_login/', views.user_login,name='user_login'),
    path('user_logout/', views.user_logout,name='user_logout'),
    path('special/', views.special,name='special'),
]
