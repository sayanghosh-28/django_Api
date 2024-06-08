from django.urls import path
from .views import start_scraping, scraping_status

urlpatterns = [
    path('start_scraping/', start_scraping, name='start_scraping'),
    path('scraping_status/<uuid:job_id>/', scraping_status, name='scraping_status'),
    
]
