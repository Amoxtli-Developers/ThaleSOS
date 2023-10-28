from django.http import HttpResponse
from django.shortcuts import render
from .audio_transcription import transcribe_audio  # Importando la función de transcripción
import os  # Import the os module
from .models import Categorie, Warning
from django.shortcuts import redirect, get_object_or_404

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

def home(request):
      return render(request, 'home.html')