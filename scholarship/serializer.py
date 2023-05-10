from rest_framework import serializers
from .models import Scholarship

class scholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields='__all__'
        