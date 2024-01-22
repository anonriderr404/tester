
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import upload_file


urlpatterns = [
	path('', views.indexView, name = 'index'),
	path('signup/', views.RegisterView, name = 'signup'),
	path('login/', views.loginView, name = 'login'),
	path('logout/', views.logoutView, name = 'logout'),
    path('upload/', upload_file, name='upload_file'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
