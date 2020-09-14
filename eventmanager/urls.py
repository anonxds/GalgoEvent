from django.urls import path

from . import views

urlpatterns = [
    path('index2/',views.index,name="index"),
    path('crear_evento/', views.crear_evento.as_view(), name="crear_evento"),
    path('fb_crear/',views.fb_crear_evento,name='fb_crear'),
    path('editar_evento/', views.ver_eventos, name='ver_eventos'),
    path('tablas/',views.tablas.as_view(),name='vertablas'),
    path('editar_evento/view/', views.ver_eventos_slot, name='ver_evento'),
    path('information/', views.informacion.as_view(), name='information'),
    path('guardar-token/', views.guardar_token, name='guardar_token'),

]
