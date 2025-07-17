from django.urls import path
from . import views
from accounts import views as accounts_views
urlpatterns = [
    path('', views.predict_career, name='home'),
    path('home/', views.home, name='landing_page'),
    path('about/', views.about, name='about'),
    path('logout/', accounts_views.logout_view, name='logout')
]
