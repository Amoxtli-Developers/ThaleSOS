from django.http import HttpResponse
from django.shortcuts import render
from .audio_transcription import transcribe_audio  # Importando la función de transcripción
from .speech_emotion import query
import os  # Import the os module
import matplotlib.pyplot as plt

import base64

audio_paths = [
    'ThalesSos/audios/prueba.wav',
    'ThalesSos/audios/prueba.wav',
    'ThalesSos/audios/prueba.wav',
    'ThalesSos/audios/Voz 001.wav',


    
]

def home(request):
    data = ""  # Initialize the data variable with an empty string
    alert_message = None  # Initialize alert_message as None
    data_emotion = ''
    model_init = query('ThalesSos/audios/prueba.wav')
    
    
    if request.method == 'POST':
        selected_audio_path = request.POST.get('selected_audio')



        if selected_audio_path:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/isaac/Downloads/imperial-data-403319-ab8beada07d0.json'

            data_emotion = query(selected_audio_path)
            print(type(data_emotion))
            categories = list(data_emotion.keys())
            values = list(data_emotion.values())

          
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

        

    return render(request, 'index.html', {'data': data, 'audio_paths': audio_paths, 'alert_message': alert_message, 'data_emotion': data_emotion, 'model_init': model_init})


def transcribe_google(request):
    if request.method == 'POST':
        audio_file = request.FILES.get('audio_file')
        if audio_file:
            # Handle the uploaded audio file
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/isaac/Downloads/imperial-data-403319-ab8beada07d0.json'
            transcript = transcribe_audio(audio_file.read())
            if transcript is not None:
                return HttpResponse(f"Transcript: {transcript}")
            else:
                return HttpResponse("Transcription failed.")
        else:
            return HttpResponse("No audio file uploaded.")
    return render(request, 'transcription_form.html')

def administrador(request):
      return render(request, 'administrador.html')
