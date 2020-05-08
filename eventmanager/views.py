from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from firebase import Firebase,firebase
from django.contrib.auth.models import User
# Create your views here.


Config = {
        "apiKey": "AIzaSyBSIAwxO5geJSslxclj68G33dZ-yumOEMI",
        "authDomain": "mapstec-81290.firebaseapp.com",
        "databaseURL": "https://mapstec-81290.firebaseio.com",
        "storageBucket": "mapstec-81290.appspot.com",
        "measurementId": "G-85RHV43HWV"
    }
_firebase = Firebase(Config)
db = _firebase.database()

class crear_evento(ListView):
    template_name = 'crear_evento.html'
    context_object_name = 'data'
    model = User

class informacion(ListView):
    pass

class tablas(ListView):
    template_name = 'buttons.html'
    context_object_name = 'data'
    model = User


def ver_eventos(request):
    data_dict = []
    users = db.child("tomas_aquino").get()
    for user in users.each():
        print("////////")
        print(user.key())
        print(user.val()['titulo'])
        print(user.val()['descripcion'])
        print(user.val()['img'])
        data_dict.append({'id':user.key(),'escuela':"tomas_aquino",'header':user.val()['header'],'titulo':user.val()['titulo'],'descripcion':user.val()['descripcion'],'img':user.val()['img']})
    print(data_dict)
    context = {
        'data':data_dict
    }
    return render(request, 'ver_eventos.html', context)

def ver_eventos_slot(request):
    if request.is_ajax():
        slot = request.POST.get('path')
        user = db.child("tomas_aquino").child(slot).get()
        data = {'id':user.key(),'escuela':"tomas_aquino",'header':user.val()['header'],'titulo':user.val()['titulo'],'descripcion':user.val()['descripcion'],'img':user.val()['img']}
        return JsonResponse(data)
    else:
        return render(request, 'tables.html')

def index(request):
    dict_cal1 = []
    dict_cal2 = []
    dict_au_1 = []
    dict_au_2 = []
    dict_am_1 = []
    dict_am_2 = []
    dict_m_1 = []
    dict_m_2 = []

    calafornix_1 = db.child("tomas_aquino").child("calafornix_1").get()
    calafornix_2 = db.child("tomas_aquino").child("calafornix_2").get()
    audiovisual_1 = db.child("tomas_aquino").child("audiovisual_1").get()
    audiovisual_2 = db.child("tomas_aquino").child("audiovisual_2").get()
    aulamagna_1 = db.child("tomas_aquino").child("aula_magna_1").get()
    aulamagna_2 = db.child("tomas_aquino").child("aula_magna_2").get()
    menu_principal_1 = db.child("tomas_aquino").child("menu_principal_1").get()
    menu_principal_2 = db.child("tomas_aquino").child("menu_principal_2").get()

    dict_cal1.append({'titulo':calafornix_1.val()['titulo'],'descripcion':calafornix_1.val()['descripcion'],'img':calafornix_1.val()['img']})
    dict_cal2.append({'titulo':calafornix_2.val()['titulo'],'descripcion':calafornix_2.val()['descripcion'],'img':calafornix_2.val()['img']})
    dict_au_1.append({'titulo':audiovisual_1.val()['titulo'],'descripcion':audiovisual_1.val()['descripcion'],'img':audiovisual_1.val()['img']})
    dict_au_2.append({'titulo':audiovisual_2.val()['titulo'],'descripcion':audiovisual_2.val()['descripcion'],'img':audiovisual_2.val()['img']})
    dict_am_1.append({'titulo':aulamagna_1.val()['titulo'],'descripcion':aulamagna_1.val()['descripcion'],'img':aulamagna_1.val()['img']})
    dict_am_2.append({'titulo':aulamagna_2.val()['titulo'],'descripcion':aulamagna_2.val()['descripcion'],'img':aulamagna_2.val()['img']})
    dict_m_1.append({'titulo':menu_principal_1.val()['titulo'],'descripcion':menu_principal_1.val()['descripcion'],'img':menu_principal_1.val()['img']})
    dict_m_2.append({'titulo':menu_principal_2.val()['titulo'],'descripcion':menu_principal_2.val()['descripcion'],'img':menu_principal_2.val()['img']})

    print(dict_au_1)
    print(dict_au_2)
    print(dict_cal2)
    print(dict_cal1)
    context = {
        'menu_1':dict_m_1,
        'menu_2':dict_m_2,
        'calafornix_1':dict_cal1,
        'calafornix_2':dict_cal2,
        'aulamagna_1':dict_am_1,
        'aulamagna_2':dict_am_2,
        'audiovisual_1':dict_au_1,
        'audiovisual_2':dict_au_2
    }

    return render(request,"index-copy.html",context)

def fb_crear_evento(request):
    if request.is_ajax():
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        img = request.POST.get('img')
        escuela = request.POST.get('escuela')
        ubicacion = request.POST.get('ubicacion')
        db = _firebase.database()
        data = {
            'titulo': titulo,
            'descripcion': descripcion,
            'img': img
        }
        print(img)
        db.child(escuela).child(ubicacion).update(data)
        return JsonResponse(data)

    else:
        return render(request, 'tables.html')

def fb_editar_evento(request):
    if request.is_ajax():
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        img = request.POST.get('img')
        escuela = request.POST.get('escuela')
        ubicacion = request.POST.get('ubicacion')
        db = _firebase.database()
        data = {
            'titulo': titulo,
            'descripcion': descripcion,
            'img': img
        }
        print(img)
        db.child(escuela).child(ubicacion).update(data)
        return JsonResponse(data)

    else:
        return render(request, 'tables.html')