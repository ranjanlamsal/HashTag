from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllTagsAPI),
    path('<pk>', views.TagAPI),
]
