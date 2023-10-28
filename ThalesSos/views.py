from django.http import HttpResponse
from django.shortcuts import render
from .audio_transcription import transcribe_audio  # Importando la función de transcripción
import os  # Import the os module

def transcribe_google(request):
    if request.method == 'POST':
        audio_file = request.FILES.get('audio_file')
        if audio_file:
            # Handle the uploaded audio file
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/salomon/Desktop/imperial-data-403319-ab8beada07d0.json'
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

def home(request):
      return render(request, 'home.html')