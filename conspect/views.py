from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import Response, APIView
from .models import *
from .serializers import *



class LessonView(APIView):

    def get(self, request):
        objects = LessonModel.objects.all()
        serializer = LessonSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.POST)
        serializer = LessonSerializer(data=request.data)
        serializer.create_json()
        return HttpResponse(status=201)


@login_required
def lessons(request):

    subjects = SubjectModel.objects.all()
    context = {'subjects': subjects}
    return render(request, 'index.html', context)
