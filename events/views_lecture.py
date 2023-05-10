from .models import Lecture
from .serializer import lectureSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from rest_framework import filters

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create(request):
    serializer = lectureSerializer(data=request.data, context={'request': request})
    if serializer.is_valid(raise_exception=ValueError):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def details(request, currId):
    try:
        details=Lecture.objects.get(id=currId)
    except details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialized_data = lectureSerializer(details, context={'request': request})
    return Response(serialized_data.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def update(request, currId):
    try:
        details=Lecture.objects.get(id=currId)
    except details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = lectureSerializer(details,data=request.data, context={'request': request})
    response_sent={}
    if serializer.is_valid():
        serializer.save()
        response_sent["success"]="Updated successfully"
        return Response(data=response_sent)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def delete(request, currId):
    try:
        details=Lecture.objects.get(id=currId)
    except details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    operation=details.delete()
    response_sent={}
    if operation:
        response_sent["success"]="Deleted Sucessfully"
    else:
        response_sent["failure"]="Deletion failed"
    return Response(data=response_sent)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def list(request):
    try:
        details=Lecture.objects.all()
    except details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialized_data = lectureSerializer(details, many=True, context={'request': request})
    return Response(serialized_data.data)

@permission_classes([IsAuthenticated])
class Search(generics.ListAPIView):
    queryset = Lecture.objects.all()
    serializer_class = lectureSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['provider', 'details']
