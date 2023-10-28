from django.shortcuts import get_object_or_404, redirect, render
from patients.models import  Result,Patient
from .models import Prescription
from .forms import DrugForm
from django.contrib.auth.decorators import login_required
# Create your views here.


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




@login_required
def drug_stock(request):
    return render(request,'pharmacy/stock.html' )