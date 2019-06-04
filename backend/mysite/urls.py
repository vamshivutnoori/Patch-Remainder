from django.contrib import admin
from django.urls import path, include
from mysite.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('CVEsearch/',views.cvesearch,name='CVE'),
    path('result/',views.output,name='script'),

]
