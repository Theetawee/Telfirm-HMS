from accounts.models import Department
from patients.models import Test

test_department_mapping = {
    'Hiv Test (HCT, RCT, VCT, PICT)': 'Microbiology',
    'BS (For mps)': 'Chemistry',
    'BS (For Microfilaria, Tryps, Leishmania)': 'Microbiology',
    'BAT': 'Chemistry',
    'Widal Test': 'Microbiology',
    'VDRL, RPR, TPHA': 'Microbiology',
    'H.Pylori Test': 'Microbiology',
    'Rheumatoid factor test': 'Immunology',
    'HBsAg Test': 'Microbiology',
    'Serum Crag (Cryptococcal antigen)': 'Microbiology',
    'CD4, & CD4%': 'Immunology',
    'Serum HCG Test': 'Chemistry',
    'Toxoplasmosis': 'Microbiology',
    'Gonnorhae': 'Microbiology',
    'Blood culture & Sensitivity': 'Microbiology',
    'Semen Analysis': 'Microbiology',
    'HIV RNA PCR (Viral Load)': 'Microbiology',
    'HVS Gram stain': 'Microbiology',
    'HVS Culture & Senstivity': 'Microbiology',
    'CBC': 'Haematology',
    'Hb': 'Haematology',
    'Sickling Test': 'Haematology',
    'ESR': 'Haematology',
    'Bleeding Time': 'Haematology',
    'Clotting Time': 'Haematology',
    'Prothrombine Time': 'Haematology',
    'Platelet Count': 'Haematology',
    'Blood Grouping': 'Haematology',
    'Lymph Zn for AFBs': 'Microbiology',
    'Lymph Gram stain': 'Microbiology',
    'Urinalysis': 'Chemistry',
    'Gram stain': 'Microbiology',
    'Culture & Senstivity': 'Microbiology',
    'Urine HCG': 'Chemistry',
    'Stool analysis (Wet/Iodine- Preparation)': 'Microbiology',
    'Stool Culture & Senstivity': 'Microbiology',
    'Modified Zn (For Oocysts)': 'Microbiology',
    'Sudan III test (For stool Fat)': 'Chemistry',
    'Sputum Zn for AFBs': 'Microbiology',
    'Sptum Culture & Senstivity': 'Microbiology',
    'Brest milk gram stain': 'Microbiology',
    'Breast milk Culture and Senstivity': 'Microbiology',
    'Biopsy Gram / Zn stain': 'Microbiology',
    'KOH + Calcoflour (fungal hypae)': 'Microbiology',
    'Biopsy Culture & Senstivity': 'Microbiology',
    'Random Blood Sugars': 'Chemistry',
    'Fasting Blood Sugars': 'Chemistry',
    'Renal Functional tests: Sodium, Potassium, Chloride, Creatine, Urea': 'Chemistry',
    'Liver Functional Tests: GOT, GPT, ALP, Alb, TP, BIL': 'Chemistry',
    'Pancreatic Functional tests (PFTs): Amylase, Lipase, Glucose': 'Chemistry',
    'Lipid Profile (LP): Cholesterol, HDL, LDL, Triglycerides': 'Chemistry'
}

for test_name, department_name in test_department_mapping.items():
    department, created = Department.objects.get_or_create(name=department_name)
    Test.objects.create(name=test_name, department=department)



from pharmacy.models import Drug

drugs = [
    "Aspirin",
    "Ibuprofen",
    "Paracetamol",
    "Amoxicillin",
    "Lisinopril",
    "Atorvastatin",
    "Simvastatin",
    "Metformin",
    "Omeprazole",
    "Ranitidine",
    "Loratadine",
    "Cetirizine",
    "Diazepam",
    "Warfarin",
    "Gabapentin",
    "Sertraline",
    "Citalopram",
    "Levothyroxine",
    "Fluoxetine",
    "Amlodipine",
]

for drug in drugs:
    n = Drug.objects.create(name=drug, stock=5)
    n.save()
