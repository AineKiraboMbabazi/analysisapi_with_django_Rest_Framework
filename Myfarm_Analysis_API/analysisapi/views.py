from django.shortcuts import render
from django.http import JsonResponse
from .models.association import Association

# Create your views here.
def create_association(request):
    pass

def get_associations_list(request):
    MAX_OBJECTS = 20
    associations = Association.objects.all()[:MAX_OBJECTS]
    
    data = {"results": list(associations.values('Location', 'creation_date', 'id', 'name', 'status', 'userId'))}
    return JsonResponse(data)