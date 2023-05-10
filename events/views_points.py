from rest_framework import routers, serializers, viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import certificateSerializer, pointSerializer
from .models import Certificate, Point, studentDetail
from rest_framework import filters

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
class pointViewSet(viewsets.ModelViewSet):
    serializer_class = pointSerializer

    def get_queryset(self):
        student = Point.objects.all()
        return student

    def create(self, request, *args, **kwargs):
        data = request.data

        new_student = Point.objects.create(
            category=data["category"], point=data['point'])

        new_student.save()

        for module in data["cert_fields"]:
            module_obj = Certificate.objects.get(certificate=module["certificate"])
            new_student.cert_field.add(module_obj)

        serializer = pointSerializer(new_student)

        return Response(serializer.data)


class certificateViewSet(viewsets.ModelViewSet):
    serializer_class = certificateSerializer

    def get_queryset(self):
        module = Certificate.objects.all()
        return module
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# @parser_classes([MultiPartParser, FormParser])
# # def Points(APIView):
# def createPoint(request):
    # curr_user=request.user
    # jsonResppts = request.data.points
    # jsonRespcat = request.data.category
    # jsontypeid  = request.data.type_id
    # jsonfile    = request.data.file
    
    # jsonRespcert={"category":jsonRespcat, "type_id":jsontypeid, "certificate":jsonfile}
    # c = Certificate.objects.create(jsonRespcert)
    # Certificate.add(c)
    # d = Certificate.save()
    
    
    # serializer = lectureSerializer(data=request.data, context={'request': request})

    # curr_user=request.user
    # point_now = Point.objects.all()
    # if point_now is None:
    #     jsonRespid = request.data.points
    #     # jsonRespcat = request.data.category
    # jsonRespcert = request.data
    #     # json={"category":jsonRespcat, "points":jsonRespid}
    #     # c = Certificate.objects.create(jsonRespcert)
    #     # Certificate.add(c)
    # serializer = certificateSerializer(data=jsonRespcert, context={'request': request})
    #     # d = Certificate.save()
    # # serializer = pointSerializer(data=json, context={'request': request})
    # # if serializer.is_valid(raise_exception=ValueError):
    #     # serializer.save(
    #     #     students_id=studentDetail.id,
    #     #     cert_field=d
    #     #     points+=query
    #     # )
    # if serializer.is_valid(raise_exception=ValueError):
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    # return Response({"message": "Sample"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def getCertificate(request):
    # try:
    curr_user=request.user
    details=Certificate.objects.filter(students=curr_user)
    # except details.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    serialized_data = certificateSerializer(details, many=True, context={'request': request})
    return Response(serialized_data.data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @parser_classes([MultiPartParser, FormParser])
# def getPoints(request):
#     try:
#         details=Certificate.objects.all()
#     except details.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serialized_data = certificateSerializer(details, context={'request': request})
#     return Response(serialized_data.data)

# class CertificateViewSet(viewsets.ModelViewSet):
#     """
#     List all workers, or create a new worker.
#     """
#     queryset = Certificate.objects.all()
#     serializer_class = certificateSerializer


# class pointSerializerViewSet(viewsets.ModelViewSet):
#     """
#     List all workkers, or create a new worker.
#     """
#     queryset = Point.objects.all()
#     serializer_class = pointSerializer