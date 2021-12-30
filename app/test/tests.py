from repertoire.models import Work, File
from django.urls import reverse
import pytest

def test_file_row(file_row):
    assert File.objects.all().count() == 1
    assert file_row.filename == "dudu.csv"
    assert file_row.work_count == 4

def test_work_create(work_row):
    assert Work.objects.all().count() == 1
    assert work_row.proprietary_id == 8
    assert work_row.iswc == "T9204649558"
    assert work_row.source == "Nollywood"
    assert work_row.title == "Home Alone"
    assert work_row.contributors == "[Dexter Daniel]"

@pytest.mark.django_db
def test_files(client):
    url = reverse("files")
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_files_details(client,file_row):
    url = reverse("file_detail", args=(file_row.id,))
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_file_works(client,file_row):
    url = reverse("file_works", args=(file_row.id,))
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_file_works_details(client,file_row, work_row):
    url = reverse("file_works_detail", args=(file_row.id, work_row.id))
    response = client.get(url)
    assert response.status_code == 200

