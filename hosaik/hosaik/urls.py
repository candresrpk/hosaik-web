
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls'), name='accounts'),
    path('blog/', include('apps.blog.urls'), name='blog'),
    path('honey/', include('apps.honey.urls'), name='honey'),
    
    
]
