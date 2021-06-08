from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from tasks.models import Task
from django.forms.models import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from tasks.serializer import TasksModelSer

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


@api_view(["GET"])
def getIndexList(request):
    indexList = Task.objects.all()

    to_json_file = serializers.serialize("json", indexList)

    return HttpResponse(to_json_file, content_type="application/json")

@api_view(["DELETE"])
def deleteIndexList(request):
    Task.objects.all().delete()

    return Response({"delete": "All objects listed at this moment are now deleted"})

@api_view(["POST"])
def postIndexList(request):
    file = 0
    parser = JSONParser().parse(request)

    serialized_json = TasksModelSer(data = parser)
    if serialized_json.is_valid() and file == 0:
        serialized_json.save()

        return JsonResponse(serialized_json.data, status=200)

    else:
        return JsonResponse(serialized_json.errors, status=404)
