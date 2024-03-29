
from django.urls import path
from .views import *

from house import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('index/', index ,name = 'index'),
    path('news/', news ,name = 'news'),
    path('<slug:url>/', views.post_category, name='post_category'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

