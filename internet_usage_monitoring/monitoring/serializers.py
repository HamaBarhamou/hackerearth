from .models import Monitoring
from rest_framework import serializers


class MonitoringSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Monitoring
        fields = ['__all__']