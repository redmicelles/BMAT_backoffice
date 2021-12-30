from django.shortcuts import get_object_or_404, render, HttpResponse
from .models import File, Work
from .serializers import FileSerializer, WorkSerializer, WorkFileSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
import json


def index(request):
    return HttpResponse("Alive an running")


class FilesList(APIView):

    """
    This retrieves listings of files
    """
    def get(self, request, format=None):

        """
        This method retrieves all file intances in the database file table
        """
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

class FilesListDetails(APIView):

    """
    This class retrieves the details of a row in the database file table
    """
    def get_object(self, pk):

        """
        This method verifies if the queried record exists
        """
        try:
            return File.objects.get(pk=pk)
        except File.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        
        file = self.get_object(pk)
        serializer = FileSerializer(file)
        return Response(serializer.data)

class WorksList(APIView):

    """
    This class retrieves all the works belonging to a queried file
    """
    def get_object(self, file_id):

        """
        This method verifies if the queried record exists
        """
        try:
            return File.objects.get(pk=file_id)
        except File.DoesNotExist:
            raise Http404

    def get(self, request, file_id, format=None):

        self.get_object(file_id)
        works = Work.objects.filter(file=file_id)
        serializer = WorkSerializer(works, many=True)

        count_works = works.count()
        file = File.objects.get(pk=file_id)
        file_data = FileSerializer(file)

        data = {
            "count": count_works,
            "works": serializer.data,
            "file": file_data.data
            }
        return Response(data)

class WorkFileList(APIView):

    """
    This class retreives the details of a specific work
    """
    def get_object(self, file_id):

        """
        This method verifies if the queried record exists
        """
        try:
            return File.objects.get(pk=file_id)
        except File.DoesNotExist:
            raise Http404

    def get(self, request, pk, file_id, format=None):
        
        self.get_object(file_id)
        work = Work.objects.filter(file=file_id).filter(pk=pk)
        serializer = WorkFileSerializer(work, many=True)
        return Response(serializer.data)
