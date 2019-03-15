from django.urls import path
import kokpit.views as views

urlpatterns = [
    path('', views.homepage, name='homepage'),

]
