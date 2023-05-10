from .models import Exam
from .serializer import examSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser

@api_view(['POST'])
@permission_classes([IsAdminUser])
@parser_classes([MultiPartParser, FormParser])
def create(request):
    serializer = examSerializer(data=request.data, context={'request': request})
    if serializer.is_valid(raise_exception=ValueError):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAdminUser])
@parser_classes([MultiPartParser, FormParser])
def details(request, currId):
    try:
        user_details=Exam.objects.get(id=currId)
    except user_details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialized_data = examSerializer(user_details, context={'request': request})
    return Response(serialized_data.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
@parser_classes([MultiPartParser, FormParser])
def update(request, currId):
    try:
        user_details=Exam.objects.get(id=currId)
    except user_details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = examSerializer(user_details,data=request.data, context={'request': request})
    response_sent={}
    if serializer.is_valid():
        serializer.save()
        response_sent["success"]="Updated successfully"
        return Response(data=response_sent)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
@parser_classes([MultiPartParser, FormParser])
def delete(request, currId):
    try:
        user_details=Exam.objects.get(id=currId)
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
def list(request):
    try:
        user_details=Exam.objects.all()
    except user_details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialized_data = examSerializer(user_details, many=True, context={'request': request})
    return Response(serialized_data.data)
