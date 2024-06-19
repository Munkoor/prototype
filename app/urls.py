from django.urls import path
from .views import TextToSpeechView

urlpatterns = [
    path('text-to-speech/', TextToSpeechView.as_view(), name='text-to-speech'),
]


app_name = "app"