
from django.contrib import admin
from django.urls import path, include
from .views import homeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='index'),
    path('accounts/', include('apps.accounts.urls'), name='accounts'),
    path('blog/', include('apps.blog.urls'), name='blog'),
    path('honey/', include('apps.honey.urls'), name='honey'),
    
    
]
