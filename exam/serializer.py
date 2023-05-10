from rest_framework import serializers
from .models import Exam

class examSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields='__all__'