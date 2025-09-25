# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employee.models import Employee
from django.http import Http404

#status gives status code or htttps response
#function based view
@api_view(['GET','POST'])
def studentsView(request):
   if request.method=='GET':
      # Get all the data from students table
      students=Student.objects.all()
      serializer=StudentSerializer(students,many=True) # passing many students so many=true
      return Response(serializer.data,status=status.HTTP_200_OK)
   elif request.method=='POST':
      serializer=StudentSerializer(data=request.data)
      if(serializer.is_valid()):
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      print(serializer.errors)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
@api_view(['GET','PUT','DELETE'])
def studentDetailsView(request,pk):
   try:
      student=Student.objects.get(pk=pk)
   except:
      return Response(status=status.HTTP_400_BAD_REQUEST)   
   
   if request.method=='GET':
      serializer=StudentSerializer(student)
      return Response(serializer.data,status=status.HTTP_201_CREATED)
   
   #this is updating data method
   elif request.method=='PUT':
      serializer=StudentSerializer(student,data=request.data)
      if(serializer.is_valid()):
         serializer.save()
         return Response(serializer.data,status=status.HTTP_200_OK)
      else:
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

   elif request.method=='DELETE':
      student.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
      
  

#calss based views
class Employees(APIView):
   def get(self,request):
      employees=Employee.objects.all()
      serializer=EmployeeSerializer(employees,many=True)
      return Response(serializer.data,status=status.HTTP_200_OK)
   
   def post(self,request):
      serializer=EmployeeSerializer(data=request.data)
      if(serializer.is_valid()):
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      print(serializer.errors)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
   def get_objects(self,pk):
      try:
         return Employee.objects.get(pk=pk)
      except Employee.DoesNotExist:
         raise Http404
      
   def get(self,request,pk):
      employee=self.get_objects(pk)
      serializer=EmployeeSerializer(employee)
      return Response(serializer.data,status=status.HTTP_200_OK)
   
   def put(self,request,pk):
      employee=self.get_objects(pk)
      serializer=EmployeeSerializer(employee,data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

   def delete(self,request,pk):
      employee=self.get_objects(pk)
      
      employee.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)   