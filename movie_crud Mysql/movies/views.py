from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from movies.models import Movie
from movies.serializers import MovieSerializer,UserSerializer
from rest_framework import status
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


# class MovieListCreate(APIView):

#     def get(self, request):
#         m = Movie.objects.all()
#         serializer_instance = MovieSerializer(m, many=True)  # added many=True
#         return Response(serializer_instance.data)

#     def post(self, request):
#         serializer_instance = MovieSerializer(data=request.data)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response({"Message": "Record Created"})
#         return Response(serializer_instance.errors)


# class MovieRetrieveUpdateDelete(APIView):

#     def get(self, request, i):
#         m = get_object_or_404(Movie, id=i)
#         serializer_instance = MovieSerializer(m) 
#         return Response(serializer_instance.data)

#     def put(self, request, i):
#         m = get_object_or_404(Movie, id=i)
#         serializer_instance = MovieSerializer(m, data=request.data)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data)
#         return Response(serializer_instance.errors)


#     def patch(self,request,i):
#         m=Movie.objects.get(id=i)
#         serializer_instance=MovieSerializer(m,request.data,partial=True)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)
        

#     def delete(self, request, i):
#         m = get_object_or_404(Movie, id=i)
#         m.delete()
#         return Response({"Message": "Deleted Successfully"})







from rest_framework import mixins

# class MovieListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)


# class MovieRetrieveUpdateDelete(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

#     queryset=Movie.objects.all()
#     serializer_class = MovieSerializer

#     def get(self,request,pk):
#         return self.retrieve(request,pk)

#     def put(self,request,pk):
#         return self.update(request,pk)

#     def patch(self,request,pk):
#         return self.partial_update(request,pk)

#     def delete(self,request,pk):
#         return self.destroy(request,pk)



from rest_framework import generics


# class MovieListCreate(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


# class MovieRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer



from rest_framework import viewsets


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



# from django.db.models import Q
# class SearchAPIView(APIView):
#     def get(self,request):
#         data=self.request.query_params.get('search')
#         m=Movie.objects.filter(Q(title__icontains=data)|
#                                 Q(director__icontains=data)|
#                                 Q(language__icontains=data))

#         if not m.exists():
#             return Response({"Message":"No Record Found"},status=status.HTTP_200_OK)
        
#         serializer_instance=MovieSerializer(m,many=True)
#         return Response(serializer_instance.errors,status=status.HTTP_200_OK)


    

from rest_framework.filters import SearchFilter

class SearchAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'director', 'language']



class RegisterAPIView(APIView):
    def post(self,request):

        form_data = request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)