from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Course
from .serializers import CourseSerializer



class CoursesList(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CoursesDetail(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer