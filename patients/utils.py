# Define choices for specialization
import random, string
from .models import Patient


RESULTS_STATUS = (("p", "Pending"), ("d", "Done"), ("c", "Confirmed"))

TEST_LEVELS = (
    ("one", "one"),  # postive/negative test
    ("two", "two"),  # needs explain
)


def create_mrn():
    while True:
        # Generate a new MRN
        initials = "".join(random.choices(string.ascii_uppercase, k=3))
        digits = "".join(random.choices(string.digits, k=9))
        new_mrn = f"P-{digits}{initials}"

        # Check if the generated MRN already exists
        if not Patient.objects.filter(mrn=new_mrn).exists():
            return new_mrn
