from rest_framework import serializers
from .models import Workshop, Lecture, Competition, Point, Certificate

class workshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields='__all__'
        
class lectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields='__all__'
        
        
class competitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields='__all__'
        
class certificateSerializer(serializers.ModelSerializer):
    students = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Certificate
        fields='__all__'
        
class pointSerializer(serializers.ModelSerializer):
    # cert_field = certificateSerializer(many=True, read_only=True)
    student = serializers.HiddenField(default=serializers.CurrentUserDefault())
    authors = serializers.PrimaryKeyRelatedField(queryset=Certificate.objects.all(), many=True) 
    class Meta:
        model = Point
        fields='__all__'