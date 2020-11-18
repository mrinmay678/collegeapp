from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Teacher,Student,User
from .serializers import TeacherSerializer,StudentSerializer,UserSerializer

class UserViewSet(APIView):
    def post(self,request):
        data=request.data
        print(data)
        user=UserSerializer()
        user.create(data)
        return Response({'message':'User created','status':True},status=200)

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer
