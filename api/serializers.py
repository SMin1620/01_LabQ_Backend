from rest_framework import serializers


class GubnSerializer(serializers.Serializer):
    gubn = serializers.IntegerField(help_text='구청코드(GUBN)')