from django.shortcuts import render, HttpResponse, redirect 
from datetime import datetime
import pickle
import os
import zipfile
import urllib.request

# Create your views here. 
def home(request): 
    current_year = datetime.now().year
    return render(request, 'index.html', {'range': range(1, 337), 'current_year': current_year})

def getPredictions(city, cdi, gender, relevent_experience, enrolled_university, education_level, major_discipline, experience, company_size, company_type, last_new_job, training_hours):

    # URL to your GitHub release (replace with your actual release link)
    url = "https://github.com/user-attachments/files/18283719/ml_model.zip"
    
    # Path to save the downloaded file
    zip_path = "/tmp/model_files.zip"

    # Download the ZIP file
    urllib.request.urlretrieve(url, zip_path)

    # Extract the ZIP file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("/tmp/")

    # Load the model and scaler from the extracted files
    model_path = "/tmp/ml_model.sav"
    scaler_path = "/tmp/scaler.sav"
    
    # Load the model and scaler using pickle
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    
    with open(scaler_path, 'rb') as scaler_file:
        scaled = pickle.load(scaler_file)
    

    prediction = model.predict(scaled.transform([
        [city, cdi, gender, relevent_experience, enrolled_university, education_level, major_discipline, experience, company_size, company_type, last_new_job, training_hours]
    ]))
    
    if prediction == 0:
        return 'no'
    elif prediction == 1:
        return 'yes'
    else:
        return 'error'
    
def result(request):
    city = int(request.GET['city'])
    cdi = float(request.GET['cdi'])
    gender = int(request.GET['gender'])
    relevent_experience = int(request.GET['relevent_experience'])
    enrolled_university = int(request.GET['enrolled_university'])
    education_level = int(request.GET['education_level'])
    major_discipline = int(request.GET['major_discipline'])
    experience = int(request.GET['experience'])
    company_size = int(request.GET['company_size'])
    company_type = int(request.GET['company_type'])
    last_new_job = int(request.GET['last_new_job'])
    training_hours = int(request.GET['training_hours'])
    
    print(city, cdi, gender, relevent_experience, enrolled_university, education_level, major_discipline, experience, company_size, company_type, last_new_job, training_hours)
    result = getPredictions(city, cdi, gender, relevent_experience, enrolled_university, education_level, major_discipline, experience, company_size, company_type, last_new_job, training_hours)
    
    
    return render(request, 'result.html', {'result': result})


def contact(request): 
    return render(request, 'contact.html')