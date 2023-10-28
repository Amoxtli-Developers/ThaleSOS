from django.http import HttpResponse
from django.shortcuts import render
import json
from .audio_transcription import transcribe_audio  # Importando la función de transcripción
from .speech_emotion import query
import os  # Import the os module
from .models import Categorie, Warning
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
import matplotlib.pyplot as plt

import base64

audio_paths = [
    'ThalesSos/audios/Voz 001.wav',
    'ThalesSos/audios/Voz 002.wav',
    'ThalesSos/audios/Tecnológico de Monterrey - Campus Ciudad de México 2.wav',
]

def home(request):
    data = ""  # Initialize the data variable with an empty string
    alert_message = None  # Initialize alert_message as None
    data_emotion = ''
    dataGraf = ''
    model_init = query('ThalesSos/audios/Voz 001.wav')
    
    
    if request.method == 'POST':
        selected_audio_path = request.POST.get('selected_audio')
        if selected_audio_path:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/isaac/Downloads/imperial-data-403319-ab8beada07d0.json'
            data_emotion = query(selected_audio_path)
            print(data_emotion)
            top1 = data_emotion[0]
            top2 = data_emotion[1]
            top3 = data_emotion[2]
            print(top1)  # Esto imprimirá 10
            print(top2)  # Esto imprimirá 10
            print(top3)
            dataGraf = [top1, top2, top3]
            print(dataGraf)

            labels= [top1['label'], top2['label'], top3['label']]
            scores = [top1['score'], top2['score'], top3['score']]

            print(labels)
            print(scores)
            variable_x = labels
            variable_y = scores
            variable_y = [int(x * 100) for x in variable_y]
            variable_x = json.dumps(variable_x)
            print("despues de  dumps",variable_x)
            

             

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
    else:
    
        variable_x = []  # Provide default values for variable_x and variable_y
        variable_y = []
        variable_y = [int(x * 100) for x in variable_y]
        variable_x = json.dumps(variable_x)
        print("despues de  dumps",variable_x)
    # Obtener todas las palabras clave
    keywords = Warning.objects.values_list('keywords', flat=True)
    
    context = {
    'data': data,
    'audio_paths': audio_paths,
    'alert_message': alert_message,
    'keywords_json': json.dumps(list(keywords)),
    'data_emotion': data_emotion,
    'model_init': model_init,
    'dataGraf': dataGraf,
    'variable_x': variable_x,
    'variable_y': variable_y,
}

    return render(request, 'index.html', context)
    

def administrador(request):
    categories = Categorie.objects.all()
    total_categorias = categories.count()
    warnings = Warning.objects.all()
    total_warnings = warnings.count()
    return render(request, 'administrador.html', {
        'warnings': warnings,
        'total_warnings': total_warnings,
        'categories': categories,
        'total_categorias': total_categorias
    })

def delete_warning(request, id):
    warning = Warning.objects.get(pk=id)
    warning.delete()
    return redirect(administrador)

def delete_categorie(request, id):
    categorie = Categorie.objects.get(pk=id)
    categorie.delete()
    return redirect(administrador)

def add_category(request):
    print("Vista add_category llamada")  # Para saber que la vista fue llamada

    if request.method == 'POST':
        category_name = request.POST.get('categoryName')
        category_message = request.POST.get('categoryMensaje')
        
        print(f"Nombre de categoría recibido: {category_name}")  # Verificar el dato recibido
        print(f"Mensaje de categoría recibido: {category_message}")  # Verificar el dato recibido
        
        Categorie.objects.create(name=category_name, message=category_message)
        
        return redirect('administrador')



def add_warning(request):
    categories = Warning.objects.all()

    if request.method == 'POST':
        keywords = request.POST.get('keywords')
        category_id = request.POST.get('category')
        category = Categorie.objects.get(id=category_id)

        Warning.objects.create(keywords=keywords, category=category)
        return redirect('administrador')  # Ejemplo: al dashboard o al listado de warnings.

    return render(request, 'administrador.html', {'categories': categories})

def update_category(request):
    if request.method == "POST":
        cat_id = request.POST.get('categoryId')
        cat_name = request.POST.get('categoryName-edited')
        cat_message = request.POST.get('categoryMensaje-edited')

        category = get_object_or_404(Categorie, id=cat_id)
        category.name = cat_name
        category.message = cat_message
        category.save()

        return redirect('administrador')

def update_warning(request):
    if request.method == "POST":
        warning_id = request.POST.get('category_id')
        keywords = request.POST.get('keywords-id')
        category_id = request.POST.get('category-nueva')

        # Obtener el objeto Warning basado en el ID
        warning_instance = Warning.objects.get(id=warning_id)

        # Actualizar los campos
        warning_instance.keywords = keywords
        warning_instance.category_id = category_id
        warning_instance.save()

        # Redireccionar (por ejemplo, a la página principal o donde prefieras)
        return redirect('administrador')

    # Si no es POST, mostrar el formulario o cualquier otra vista.
    return render(request, 'administrador.html', {})