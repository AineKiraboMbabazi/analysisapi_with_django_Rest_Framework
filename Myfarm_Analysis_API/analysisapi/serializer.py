from rest_framework import serializers
from .models.association import Association
from .models.government import Government



class AssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Association
        fields = '__all__'

class GovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Government
        fields = '__all__'