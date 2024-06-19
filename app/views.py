from io import BytesIO
from pathlib import Path

import openai
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from AIproject import settings
from .serializers import TextToSpeechSerializer
from openai import OpenAI


class TextToSpeechView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TextToSpeechSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            client = OpenAI(api_key='sk-proj-bXXAAFJWfd2Bc5RUF61hT3BlbkFJwFWsgAns3347cSeAbCEH')
            audio_buffer = bytearray()

            with client.audio.speech.with_streaming_response.create(
                    model="tts-1",
                    voice="alloy",
                    response_format="mp3",
                    input=text
            ) as response:
                for chunk in response.iter_bytes(chunk_size=1024):
                    audio_buffer.extend(chunk)

            return HttpResponse(bytes(audio_buffer), content_type="audio/mp3")


