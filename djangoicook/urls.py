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



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', views.Register_api.as_view(), name='register'),
    # path('api/login/', views.UserLogoutAPIView.as_view, name='login'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/categories/', views.Catapilist.as_view(), name='categories'),
    path('api/addcategories/', views.Categoriescreate.as_view(), name='addcategories'),
    path('api/addrecipes/',views.RecipesCreateView.as_view(), name='addrecipes'),
    path('api/recipes/',views.Recipesapilist.as_view(), name='recipes'),
    path('api/myrecipes/',views.RecipesOwner.as_view(), name='myrecipes'),
    path('api/updaterecipes/<int:pk>/',views.RecipesUpdate.as_view(), name='updaterecipes'),
    path('api/deleterecipes/<int:pk>/',views.RecipeDelete.as_view(), name='Deleterecipes'),
    
    path('api/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)