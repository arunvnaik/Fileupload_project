from django.shortcuts import render
import pandas as pd
from filereaderupload_app.forms import FileUploadForm
from django.http import HttpResponse


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            if file.name.endswith('.csv'):
                data = pd.read_csv(file)
            elif file.name.endswith('.xlsx'):
                data = pd.read_excel(file)
            else:
                return HttpResponse("File type not supported")
            
            # Process the data here (for now we will just return it as a response)
            return HttpResponse(data.to_html())
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})

from django.middleware.csrf import get_token
from django.http import JsonResponse

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})
