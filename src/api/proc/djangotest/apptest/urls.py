from django.urls import path

from . import views
from .views import query1,query2,query3,query4

urlpatterns = [
    path("", views.index, name="index"),
    path('query1/', query1, name='query1'),
    path('query2/<title>/<filename>/', query2, name='query2'),
    path('query3/<date>/<filename>/', query3, name='query3'),
    path('query4/<artist>/<filename>/', query4, name='query4'),
]
