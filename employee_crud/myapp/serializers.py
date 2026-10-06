from rest_framework import serializers
from myapp.models import Employee

# class EmployeeSerializer(serializers.Serializer): 
    
#     empid=serializers.IntegerField() 
#     name=serializers.CharField(max_length=20)
#     age=serializers.IntegerField()
#     place=serializers.CharField(max_length=20)

#     gender_choices=[
#         ('male','Male'),('female','Female')
#     ]

#     # Changed from CharField to ChoiceField
#     gender=serializers.ChoiceField(choices=gender_choices) 

#     joining_date=serializers.DateField()

#     salary=serializers.IntegerField()
#     designation=serializers.CharField(max_length=20)
#     image=serializers.ImageField(upload_to="image",null=True)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


    def create(self, validated_data):
        
        return Employee.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.empid = validated_data.get('empid', instance.empid)
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.place = validated_data.get('place', instance.place)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.joining_date = validated_data.get('joining_date', instance.joining_date)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.image = validated_data.get('image', instance.image)

        instance.save()
        return instance


    def validate(self, data):
            if data.get("age") is not None and data["age"] <= 0:
                raise serializers.ValidationError({
                    "age": "Age must be a positive integer greater than zero."
                })
            return data
