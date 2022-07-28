from rest_framework import serializers


class GubnSerializer(serializers.Serializer):

    """
    author : 이승민
    param : gubn
    explanation :
        - swagger에서 query param을 입력하기 위해 구현한 serializer입니다.
    """

    gubn = serializers.IntegerField(help_text='구청코드(GUBN)')