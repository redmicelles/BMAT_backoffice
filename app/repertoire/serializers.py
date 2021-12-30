from rest_framework import serializers
from .models import File, Work
import json
from rest_framework.renderers import JSONRenderer

class FileSerializer(serializers.ModelSerializer):

    """Some text"""
    class Meta:

        model = File
        fields = "__all__"

class WorkSerializer(serializers.ModelSerializer):

    """
    This class serializes the Work Model
    """
    contributors = serializers.SerializerMethodField(source="contributors", read_only=True)

    def get_contributors(self, instance):

        """
        This method formats the contributors field
        """
        if "|" in instance.contributors:
            return instance.contributors.replace("[", "").replace("]", "").split("|")
        return [instance.contributors.replace("[", "").replace("]", ""),]

    class Meta:

        model = Work
        fields =(
                    "id",
                    "proprietary_id",
                    "iswc",
                    "source",
                    "title",
                    "contributors",
                )

class WorkFileSerializer(serializers.ModelSerializer):

    """Some text"""
    class Meta:

        model = Work
        fields = "__all__"