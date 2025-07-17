from django.urls import path
from . import views
from recommender.views import home
urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', home, name='home'),
]
