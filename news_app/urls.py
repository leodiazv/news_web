from unicodedata import name
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about_us', views.about_us, name='about_us'),
    path('create_new', views.create_new, name='create_new'),
    path('edit_new/<int:id>', views.edit_new, name='edit_new'),
    path('delete_news/<int:id>', views.delete_news, name='delete_news'),
    path('news_detail/<int:id>', views.news_detail, name='news_detail')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)