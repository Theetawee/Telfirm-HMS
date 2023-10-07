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

PARASITOLOGY_TESTS_CHOICES = [
    ("Malaria Smear", "Malaria Smear"),
    ("Stool Ova and Parasite (O&P) Exam", "Stool Ova and Parasite (O&P) Exam"),
    ("Giardia Antigen Test", "Giardia Antigen Test"),
    ("Trichomonas Wet Prep", "Trichomonas Wet Prep"),
    ("Toxoplasma IgG/IgM", "Toxoplasma IgG/IgM"),
    ("Cryptosporidium Antigen Test", "Cryptosporidium Antigen Test"),
    ("Schistosoma Antibody Test", "Schistosoma Antibody Test"),
    ("Filariasis Blood Smear", "Filariasis Blood Smear"),
]

# Medical tests in Microbiology department
MICROBIOLOGY_TESTS_CHOICES = [
    ("Bacterial Culture and Sensitivity (C&S)", "Bacterial Culture and Sensitivity (C&S)"),
    ("Urine Culture", "Urine Culture"),
    ("Blood Culture", "Blood Culture"),
    ("Fungal Culture", "Fungal Culture"),
    ("Stool Culture", "Stool Culture"),
    ("Wound Culture", "Wound Culture"),
    ("Viral Culture", "Viral Culture"),
    ("Gram Stain", "Gram Stain"),
    ("Acid-Fast Bacillus (AFB) Stain", "Acid-Fast Bacillus (AFB) Stain"),
    ("Antimicrobial Susceptibility Testing", "Antimicrobial Susceptibility Testing"),
]

HAEMATOLOGY_TESTS_CHOICES = [
    ("Complete Blood Count (CBC)", "Complete Blood Count (CBC)"),
    ("Hemoglobin Electrophoresis", "Hemoglobin Electrophoresis"),
    ("Coagulation Profile", "Coagulation Profile"),
    ("Blood Film Examination", "Blood Film Examination"),
    ("Erythrocyte Sedimentation Rate (ESR)", "Erythrocyte Sedimentation Rate (ESR)"),
    ("Peripheral Blood Smear", "Peripheral Blood Smear"),
    ("Bone Marrow Aspiration and Biopsy", "Bone Marrow Aspiration and Biopsy"),
]


CHEMISTRY_TESTS_CHOICES = [
    ("Basic Metabolic Panel (BMP)", "Basic Metabolic Panel (BMP)"),
    ("Comprehensive Metabolic Panel (CMP)", "Comprehensive Metabolic Panel (CMP)"),
    ("Liver Function Tests (LFTs)", "Liver Function Tests (LFTs)"),
    ("Lipid Profile", "Lipid Profile"),
    ("Glucose Tolerance Test (GTT)", "Glucose Tolerance Test (GTT)"),
    ("Thyroid Function Tests", "Thyroid Function Tests"),
    ("Cardiac Enzyme Tests", "Cardiac Enzyme Tests"),
    ("Electrolyte Panel", "Electrolyte Panel"),
]

IMMUNOLOGY_TESTS_CHOICES = [
    ("HIV Antibody Test", "HIV Antibody Test"),
    ("Hepatitis B Surface Antigen (HBsAg)", "Hepatitis B Surface Antigen (HBsAg)"),
    ("C-reactive Protein (CRP)", "C-reactive Protein (CRP)"),
    ("Rheumatoid Factor (RF)", "Rheumatoid Factor (RF)"),
    ("Antinuclear Antibody (ANA) Test", "Antinuclear Antibody (ANA) Test"),
    ("Allergy Testing (IgE)", "Allergy Testing (IgE)"),
    ("Immunoglobulin G (IgG) Test", "Immunoglobulin G (IgG) Test"),
    ("Tumor Markers", "Tumor Markers"),
]
