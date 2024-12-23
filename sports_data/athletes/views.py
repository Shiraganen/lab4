import os
from django.shortcuts import render, redirect
from django.conf import settings
from sports_data.settings import BASE_DIR
from .forms import AthleteForm
from .models import Athlete
from .utils import save_json_to_folder, save_xml_to_folder, validate_json_file, validate_xml_file
import os



UPLOAD_FOLDER = os.path.join(settings.MEDIA_ROOT, 'uploads')

def home(request):
    return render(request, 'athletes/home.html')

def add_athlete(request):
    if request.method == 'POST':
        form = AthleteForm(request.POST)
        if form.is_valid():
            athlete = form.save(commit=False)
            athlete.save()
            data = {
                'first_name': athlete.first_name,
                'last_name': athlete.last_name,
                'age': athlete.age,
                'sport': athlete.sport,
                'country': athlete.country,
            }
            # Сохранение данных в файл
            save_json_to_folder([data], UPLOAD_FOLDER, f"{athlete.first_name}_{athlete.last_name}.json")
            return redirect('home')
    else:
        form = AthleteForm()
    return render(request, 'athletes/add_athlete.html', {'form': form})

def upload_file(request):
    if request.method == 'POST' and request.FILES:
        uploaded_file = request.FILES['file']
        # Обработать файл (сохранить или выполнить другие действия)
    return render(request, 'upload_file.html')
def list_files(request):
    
    upload_dir = os.path.join(settings.BASE_DIR, 'uploads')

    
    if not os.path.exists(upload_dir):
        return render(request, 'athletes/list_files.html', {'error': 'No files uploaded yet.'})

    
    files = os.listdir(upload_dir)

    return render(request, 'athletes/list_files.html', {'files': files})


UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')


if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


