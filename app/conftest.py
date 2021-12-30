import pytest
from repertoire.models import Work, File

@pytest.fixture()
def file_row(db):
    return File.objects.create(
        filename = "dudu.csv",
        work_count = 4,
        )

@pytest.fixture()
def work_row(db, file_row):
    return Work.objects.create(
        proprietary_id = 8,
        iswc = "T9204649558",
        source = "Nollywood",
        title = "Home Alone",
        contributors = f"[Dexter Daniel]",
        file = file_row
    )
