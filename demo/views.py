from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages, admin
from django.utils.html import format_html


class Request(models.Model):

    body = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Request recibido'
        verbose_name_plural = 'Requests recibidos'


class RequestAdmin(admin.ModelAdmin):
    list_display = ('visor', 'id')
    list_per_page = 10

    def visor(self, obj):
        return format_html('<a href="/admin/demo/request/'
                           'ver_request?id={id}">{msg}</a>', id=obj.id,
                           msg='VER')



def ver_request(request):
    id = request.GET.get('id', False)
    if not id:
        messages.add_message(request, messages.ERROR, 'Request no encontrado')
        return redirect('/admin/demo/request')
    try:
        req = Request.objects.get(id=id)

        return render(request, 'ver_request.html', context={"req": req})
    except:
        messages.add_message(request, messages.ERROR, 'Request no encontrado')
        return redirect('/admin/demo/request')



class Demo(APIView):

    def get(self, request, format=None):
        return Response({"detalle": "Bienvenido al API! haga POST"})

    def post(self, request, format=None):
        try:
            bod = json.loads(request.body)
            try:
                niu = Request(body=str(bod).replace("'", '"'))
                niu.save()
            except:
                pass
            return Response({"detalle": bod})
        except:
            return Response({"detalle": "JSON no reconocido"})
