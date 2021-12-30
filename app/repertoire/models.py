from django.db import models

# Create your models here.

class File(models.Model):

    """Some comment here"""
    filename = models.CharField(max_length=255, unique=True)
    work_count = models.IntegerField()
    
    def __str__(self):

        """Some comment here"""
        return self.filename

class Work(models.Model):

    """Some comment here"""
    proprietary_id = models.IntegerField()
    iswc = models.CharField(max_length=255, null=False)
    source = models.CharField(max_length=255, null=False)
    title = models.CharField(max_length=255, null=False)
    contributors = models.CharField(max_length=255, null=False)
    file = models.ForeignKey(File, on_delete=models.CASCADE)

    def __str__(self):

        """Some comment here"""
        return f"{self.title} {self.contributors}"
    
    

