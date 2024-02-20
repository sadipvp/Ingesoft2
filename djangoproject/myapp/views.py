from django.http import HttpResponse, JsonResponse
from .models import Project
from rest_framework import serializers


# Create your views here.

class MiModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

def Index(request):
    return HttpResponse("<h1> index </h2>")

def Hello(request,username):
    print(username)
    return HttpResponse("<h2>Hello %s</h2>" % username)

def Projects(request):
    projects = list(Project.objects.all())
    serializer = MiModeloSerializer(projects, many=True)
    return JsonResponse(projects, safe=False)

def About(request):
    return HttpResponse("About")