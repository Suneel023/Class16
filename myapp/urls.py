from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('form/',views.builtinforms,name="builtinform"),
]