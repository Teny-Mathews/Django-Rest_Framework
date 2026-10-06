from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from myapp.models import Employee
from myapp.serializers import EmployeeSerializer


class Employeelist(APIView):
    def get(self, request):
        e = Employee.objects.all()
        serializer_instance = EmployeeSerializer(e, many=True)
        return Response(data=serializer_instance.data, status=status.HTTP_200_OK)


class Employeecreate(APIView):
    def post(self, request):
        serializer_instance = EmployeeSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(
                {"Message": "created", "data": serializer_instance.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)


class Employeeretrieve(APIView):
    def get(self, request, id): 
        e = get_object_or_404(Employee, id=id)
        serializer_instance = EmployeeSerializer(e)
        return Response(serializer_instance.data, status=status.HTTP_200_OK)


class Employeefullupdate(APIView):
    def put(self, request, id):  
        e = get_object_or_404(Employee, id=id)
        serializer_instance = EmployeeSerializer(e, data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_200_OK)
        return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)


class Employeepartialupdate(APIView):
    def patch(self, request, id):  
        e = get_object_or_404(Employee, id=id)
        serializer_instance = EmployeeSerializer(e, data=request.data, partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_200_OK)
        return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDelete(APIView):
    def delete(self, request, id):  
        e = get_object_or_404(Employee, id=id)
        e.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  