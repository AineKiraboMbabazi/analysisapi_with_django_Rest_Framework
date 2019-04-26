from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models.association import Association
from .models.government import Government
from .serializer import AssociationSerializer,GovernmentSerializer



class AssociationList(generics.ListCreateAPIView):
    queryset = Association.objects.all()
    serializer_class = AssociationSerializer

class AssociationDetail(generics.RetrieveDestroyAPIView):
    queryset = Association.objects.all()
    serializer_class = AssociationSerializer

class GovernmentList(generics.ListCreateAPIView):
    queryset = Government.objects.all()
    serializer_class = GovernmentSerializer

class GovernmentDetail(generics.RetrieveDestroyAPIView):
    queryset = Government.objects.all()
    serializer_class = GovernmentSerializer
