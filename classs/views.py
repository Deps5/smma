from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


class StudentList(APIView):

    def get(self, request):
        student_list = Student.objects.all()
        serializer = StudentSerializer(student_list, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            print("IS VALIDDDD")
            serializer.save()
        return Response(serializer.data)

def home(request):
    return render(request, "classs/index.html")
