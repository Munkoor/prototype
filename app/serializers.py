from rest_framework import serializers


class TextToSpeechSerializer(serializers.Serializer):
    text = serializers.CharField()