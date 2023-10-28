from django.http import HttpResponse
from django.shortcuts import render
from .audio_transcription import transcribe_audio  # Importando la función de transcripción
import os  # Import the os module

import base64

audio_paths = [
    'ThalesSos/audios/Voz 001.wav',
    'ThalesSos/audios/Voz 002.wav',
]

def home(request):
    data = ""  # Initialize the data variable with an empty string
    alert_message = None  # Initialize alert_message as None
    
    if request.method == 'POST':
        selected_audio_path = request.POST.get('selected_audio')
        if selected_audio_path:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/salomon/Desktop/imperial-data-403319-ab8beada07d0.json'

            with open(selected_audio_path, 'rb') as audio_file:
                # Encode the audio data as base64
                audio_data = base64.b64encode(audio_file.read()).decode('utf-8')

            transcript = transcribe_audio(audio_data)  # Pass the base64-encoded audio data
            if transcript is not None:
                data = transcript  # Assign the transcript to the data variable
            else:
                alert_message = "Transcription failed."
        else:
            alert_message = "Ningun archivo seleccionado"

    return render(request, 'index.html', {'data': data, 'audio_paths': audio_paths, 'alert_message': alert_message})

def administrador(request):
      return render(request, 'administrador.html')
  
  
