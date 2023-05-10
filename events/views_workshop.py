from .models import Workshop
from .serializer import workshopSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create(request):
    serializer = workshopSerializer(data=request.data, context={'request': request})
    if serializer.is_valid(raise_exception=ValueError):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def details(request, currId):
    try:
        details=Workshop.objects.get(id=currId)
    except details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialized_data = workshopSerializer(details, context={'request': request})
    return Response(serialized_data.data)

@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def update(request, currId):
    try:
        details=Workshop.objects.get(id=currId)
    except details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = workshopSerializer(details,data=request.data, context={'request': request})
    response_sent={}
    if serializer.is_valid():
        serializer.save()
        response_sent["success"]="Updated successfully"
        return Response(data=response_sent)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def delete(request, currId):
    try:
        details=Workshop.objects.get(id=currId)
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
# @permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def list(request):
    try:
        details=Workshop.objects.all()
    except details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialized_data = workshopSerializer(details, many=True, context={'request': request})
    return Response(serialized_data.data)

# @permission_classes([IsAuthenticated])
class Search(generics.ListAPIView):
    queryset = Workshop.objects.all()
    serializer_class = workshopSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['provider', 'details', 'name']
    
@api_view(["POST"])
def filter(request):
    # try:
        result=[]
        fields=request.data["interest"]
        for field in fields:
            temp = Workshop.objects.filter(category=field)
            for i in temp:   
                result.append(i)
            
        serialized_data = workshopSerializer(result, many=True, context={'request': request})
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    # except:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    
# https://www.django-rest-framework.org/api-guide/filtering/#filtering-against-query-parameters
# class SearchList(generics.ListAPIView):
#     serializer_class = workshopSerializer

#     def get_queryset(self):
#         queryset = Workshop.objects.all()
#         category = self.request.query_params.get('category')
#         if category is not None:
#             queryset = queryset.filter(purchaser__username=username)
#         return queryset

# class ProductList(generics.ListAPIView):
#     queryset = Workshop.objects.all()
#     serializer_class = workshopSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['   ', 'in_stock']
