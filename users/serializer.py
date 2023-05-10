from rest_framework import serializers
from .models import studentDetail, promoterDetail, facultyDetail

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import User

# Added custom serializer for adding first name
# https://stackoverflow.com/questions/62291394/django-rest-auth-dj-rest-auth-custom-user-registration
class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField()

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', '')
        }
            
class studentdetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    first_name=serializers.CharField(source='user.first_name')
    class Meta:
        model = studentDetail
        # fields='__all__'
        fields = ('user', 'phone_no', 'course', 'gender', 'clas', 'avatar', 'rollno', 'interest', 'inst', 'first_name', 'credit_ac', 'credit_es')


class promoterdetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = promoterDetail
        fields='__all__'
        
class facultyDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = facultyDetail
        fields='__all__'