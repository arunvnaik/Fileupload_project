from django.urls import path
from filereaderupload_app.views import upload_file,get_csrf_token

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
]
