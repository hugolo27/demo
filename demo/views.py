from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from django.db import models


class Request(models.Model):

    body = models.TextField(null=True, blank=True)

class Demo(APIView):

    def get(self, request, format=None):
        return Response({"detalle": "Bienvenido al API! haga POST"})

    def post(self, request, format=None):
        try:
            bod = json.loads(request.body)
            try:
                niu = Request(body=str(bod))
                niu.save()
            except:
                pass
            return Response({"detalle": bod})
        except:
            return Response({"detalle": "JSON no reconocido"})
