from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
# Create your views here.
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseBadRequest
from django.core import serializers
import json
from fcm_django.models import FCMDevice

@csrf_exempt
@require_http_methods(["POST"])
def guardar_token(request):
    print("dsd")
    _devide = FCMDevice.objects.filter(active=True)
    _devide.send_message(title="title", body="desciprfs")
    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)

    token = bodyDict['token']

    existe = FCMDevice.objects.filter(registration_id = token,active=True)
    if len(existe) > 0:
        return HttpResponseBadRequest(json.dumps({"mensaje":"token"}))
    device = FCMDevice()
    device.registration_id = token
    device.active = True

    if request.user.is_authenticated:
        device.user = request.user

    device.save()

    return HttpResponse(json.dumps({"mensaje": "token"}))


Config = {
        "apiKey": "AIzaSyBSIAwxO5geJSslxclj68G33dZ-yumOEMI",
        "authDomain": "mapstec-81290.firebaseapp.com",
        "databaseURL": "https://mapstec-81290.firebaseio.com",
        "storageBucket": "mapstec-81290.appspot.com",
        "measurementId": "G-85RHV43HWV"
    }
_firebase = None
db = None

class crear_evento(ListView):
    template_name = 'crear_evento.html'
    context_object_name = 'data'
    model = User

class informacion(ListView):
    template_name = 'information.html'
    context_object_name = 'data'
    model = User

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
    context = {
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
        print('this is my text ',escuela)
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