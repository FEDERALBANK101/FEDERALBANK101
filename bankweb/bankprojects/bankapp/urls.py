
from django.urls import path

from bankapp import views
app_name='bankapp'

urlpatterns=[

    path('',views.homepage,name='homepage'),
    path('login/',views.login,name='login'),
    path('Register/',views.Register,name='Register'),
    path('logout/',views.logout,name='logout'),
    path('formpage/',views.formpage,name='formpage'),
    path('form/',views.form,name='form'),
    path('services/',views.service,name='service'),
    path('success/',views.success,name="success"),
]

