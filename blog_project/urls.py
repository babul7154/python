from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('blog.urls')),
    path('accounts/', include('accounts.urls'))
    #!  note --if  I use  path('accounts/', include('accounts.urls'))  all accounts url  will start  from http://127.0.0.1:8000/accounts/xyz/
    #!  if  I use   path('accounts/', include('accounts.urls'))  all accounts url  will start  from http://127.0.0.1:8000/xyz/  
    #? big difference nah
]
