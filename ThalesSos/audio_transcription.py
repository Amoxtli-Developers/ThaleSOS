from google.cloud import speech_v1p1beta1 as speech
from decouple import config

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
GOOGLE_APPLICATION_CREDENTIALS = config('GOOGLE_APPLICATION_CREDENTIALS')

def transcribe_audio(audio_data):
    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(content=audio_data)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="es-MX",
    )

    try:
        response = client.recognize(config=config, audio=audio)
        transcript = ""
        for result in response.results:
            transcript += result.alternatives[0].transcript + " "

        return transcript
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

