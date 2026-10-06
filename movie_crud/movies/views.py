from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from movies.models import Movie
from movies.serializers import MovieSerializer
from django.shortcuts import get_object_or_404

# class Movielist(APIView):
#     def get(self,request):

#         m=Movie.objects.all()

#         serializer_instance=MovieSerializer(m,many=True)

#         return Response(data=serializer_instance.data)

# class Moviecreate(APIView):
#     def post(self,request):

#         serializer_instance=MovieSerializer(data=request.data)

#         if serializer_instance.is_valid():
#             if serializer_instance.save():
#                 return Response({"Message":"Record Created"})
#             else:
#                 return Response(serializer_instance.errors)


class MovieListCreate(APIView):

    def get(self, request):
        m = Movie.objects.all()
        serializer_instance = MovieSerializer(m, many=True)  # added many=True
        return Response(serializer_instance.data)

    def post(self, request):
        serializer_instance = MovieSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"Message": "Record Created"})
        return Response(serializer_instance.errors)


class MovieRetrieveUpdateDelete(APIView):

    def get(self, request, i):
        m = get_object_or_404(Movie, id=i)
        serializer_instance = MovieSerializer(m) 
        return Response(serializer_instance.data)

    def put(self, request, i):
        m = get_object_or_404(Movie, id=i)
        serializer_instance = MovieSerializer(m, data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        return Response(serializer_instance.errors)


    def patch(self,request,i):
        m=Movie.objects.get(id=i)
        serializer_instance=MovieSerializer(m,request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
        

    def delete(self, request, i):
        m = get_object_or_404(Movie, id=i)
        m.delete()
        return Response({"Message": "Deleted Successfully"})