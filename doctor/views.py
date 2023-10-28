from django.shortcuts import get_object_or_404, redirect, render

from patients.models import Patient, Result

from django.db.models import Count, F
from pharmacy.forms import DrugForm
from django.contrib.auth.decorators import login_required
from pharmacy.models import Prescription



def index(request):
    # Get patients with all results marked as done
    patients = Patient.objects.annotate(
        total_results=Count('result'),
        done_results=Count('result', filter=F('result__done'))
    ).filter(total_results=F('done_results'))

    return render(request, 'doctor/index.html', {'patients': patients})



@login_required
def prescribe_drug(request, patient_id):
    result = get_object_or_404(Result, pk=patient_id)
    pres = Prescription.objects.filter(patient=result.patient)

    if request.method == 'POST':
        form = DrugForm(request.POST)
        if form.is_valid():
            drugs = form.cleaned_data['drugs']
            detail = form.cleaned_data['detail']

            if pres.exists():
                prescription = pres.first()
            else:
                prescription = Prescription.objects.create(patient=result.patient, detail=detail)

            # Set the selected drugs for the prescription
            prescription.drugs.add(*drugs)  # Use the * to unpack the list

            return redirect('pharm', patient_id=patient_id)

    else:
        form = DrugForm()

    context = {
        "result": result,
        "form": form,
        "pres": pres.first()
    }
    return render(request, 'pharmacy/index.html', context)

