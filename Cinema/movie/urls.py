from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', HomeView, name='home'),
    path('movie-detail-<int:id>/', MovieDetail, name='MovieDetail')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)