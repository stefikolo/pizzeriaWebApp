from django.urls import path
import kokpit.views as views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('menu/', views.menu, name='menu'),
    path('promocje/', views.promocje, name='promocje'),
    path('lokale/', views.lokale, name='lokale'),
    path('o_firmie/', views.o_firmie, name='o_firmie'),
    path('dzieje_sie/', views.dzieje_sie, name='dzieje_sie'),
    path('franczyza/', views.franczyza, name='franczyza'),
    path('kariera/', views.kariera, name='kariera'),
    path('partnerzy/', views.partnerzy, name='partnerzy'),
    path('opinie/', views.opinie, name='opinie'),
    path('regulamin/', views.regulamin, name='regulamin'),
    path('handmade_and_fresh/', views.handmade_and_fresh, name='handmade_and_fresh'),
    path('alergeny/', views.alergeny, name='alergeny'),
    path('tabela_kalorii/', views.tabela_kalorii, name='tabela_kalorii'),
    path('kontakt/', views.kontakt, name='kontakt'),
path('zamowienia/', views.zamowienia, name='zamowienia'),
]
