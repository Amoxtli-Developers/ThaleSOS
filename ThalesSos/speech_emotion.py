import requests

API_URL = "https://api-inference.huggingface.co/models/DunnBC22/wav2vec2-base-Speech_Emotion_Recognition"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

