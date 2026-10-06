from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from myrecipe.models import Recipe
from myrecipe.serializers import RecipeSerializer


class Recipelist(APIView):
    def get(self, request):
        r = Recipe.objects.all()
        serializer = RecipeSerializer(r, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class Recipecreate(APIView):
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class Reciperetrieve(APIView):
    def get(self, request, id):
        r = get_object_or_404(Recipe, id=id)
        serializer = RecipeSerializer(r)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Recipefullupdate(APIView):
    def put(self, request, id): 
        r = get_object_or_404(Recipe, id=id)
        serializer = RecipeSerializer(r, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Record Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Recipepartialupdate(APIView):
    def put(self, request, id): 
        r = get_object_or_404(Recipe, id=id)
        serializer = RecipeSerializer(r, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Record Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Recipedelete(APIView):
    def delete(self, request, id):  
        recipe = get_object_or_404(Recipe, id=id)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  