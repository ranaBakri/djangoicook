"""djangoicook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from djicook import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from knox import views as knox_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', views.Register_api.as_view(), name='register'),
    path('api/login/', views.Login_api, name='login'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/categories/', views.Catapilist.as_view(), name='categories'),
    path('api/createcategories/', views.Categoriescreate.as_view(), name='createcategories'),
    path('api/createrecipes/',views.RecipesCreateView.as_view(), name='createrecipes'),
    path('api/recipes/',views.Recipesapilist.as_view(), name='recipes'),
     path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)