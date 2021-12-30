from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index),
    path('files/', views.FilesList.as_view(), name="files"),
    path('files/<int:pk>', views.FilesListDetails.as_view(), name="file_detail"),
    path('files/<int:file_id>/works', views.WorksList.as_view(), name="file_works"),
    path('files/<int:file_id>/works/<int:pk>', views.WorkFileList.as_view(), name="file_works_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)