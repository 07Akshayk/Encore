from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

from .serializer import promoterdetailSerializer
from .models import promoterDetail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://127.0.0.1:8000/user/google"
    client_class = OAuth2Client
      

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
# https://stackoverflow.com/questions/27934822/get-current-user-in-model-serializer
def createProfile(request):
    curr_user=request.user
    serializer = promoterdetailSerializer(data=request.data, context={'request': request})
    if serializer.is_valid(raise_exception=ValueError):
        serializer.save(
            user_id=curr_user.id
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def details(request):
    try:
        curr_user=request.user
        user_details=promoterDetail.objects.get(user=curr_user)
    except user_details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialized_data = promoterdetailSerializer(user_details, context={'request': request})
    return Response(serialized_data.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def updateDetails(request):
    try:
        curr_user=request.user
        user_details=promoterDetail.objects.get(user=curr_user)
    except user_details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = promoterdetailSerializer(user_details,data=request.data, context={'request': request})
    response_sent={}
    if serializer.is_valid():
        serializer.save()
        response_sent["success"]="Updated successfully"
        return Response(data=response_sent)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def deleteDetails(request):
    try:
        curr_user=request.user
        user_details=promoterDetail.objects.get(user=curr_user)
    except user_details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    operation=user_details.delete()
    response_sent={}
    if operation:
        response_sent["success"]="Deleted Sucessfully"
    else:
        response_sent["failure"]="Deletion failed"
    return Response(data=response_sent)

@api_view(['GET'])
@permission_classes([IsAdminUser])
@parser_classes([MultiPartParser, FormParser])
def listDetails(request):
    try:
        user_details=promoterDetail.objects.all()
    except user_details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialized_data = promoterdetailSerializer(user_details, many=True, context={'request': request})
    return Response(serialized_data.data)