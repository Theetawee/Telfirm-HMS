# Define choices for specialization
CARDIOLOGIST = 'Cardiologist'
NEUROLOGIST = 'Neurologist'
SURGEON = 'Surgeon'
PEDIATRICIAN = 'Pediatrician'
OTHER = 'Other'

SPECIALIZATION_CHOICES = [
    (CARDIOLOGIST, 'Cardiologist'),
    (NEUROLOGIST, 'Neurologist'),
    (SURGEON, 'Surgeon'),
    (PEDIATRICIAN, 'Pediatrician'),
    (OTHER, 'Other'),
]


GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

STATUS_CHOICES = (
    ('A', 'Admitted'),
    ('D', 'Discharged'),
    ('O', 'Other'),
)

WARD=(
    ('OPD','OPD'),
    ('IPD','IPD')
)

RESULTS_FAST=(
    ('POSTIVE','POSTIVE'),
    ('NEGATIVE','NEGATIVE')
)

RESULTS_STATUS=(
    ('p','Pending'),
    ('d','Done'),
    ('c','Confirmed')
)

TEST_LEVELS=(
    ('one','one'),#postive/negative test
    ('two','two'),#needs explain
    
)