from rest_framework import serializers
from movies.models import Movie

# class MovieSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=20)
#     director = serializers.CharField(max_length=20)
#     language = serializers.CharField(max_length=20)
#     year = serializers.IntegerField()
#     rating = serializers.FloatField()
#     runtime = serializers.IntegerField()


#     def create(self, validated_data):
        
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.director = validated_data.get('director', instance.director)
#         instance.language = validated_data.get('language', instance.language)
#         instance.year = validated_data.get('year', instance.year)
#         instance.rating = validated_data.get('rating', instance.rating)
#         instance.runtime = validated_data.get('runtime', instance.runtime)
#         instance.save()
#         return instance



class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        
        model=Movie

        fields="__all__"

