from django.shortcuts import get_object_or_404, redirect, render
from patients.models import  Result,Patient
from .models import Prescription
from .forms import DrugForm
# Create your views here.


def prescribe_drug(request, result_id):
    result = get_object_or_404(Result, pk=result_id)
    pres = Prescription.objects.filter(patient=result.patient)

    if request.method == 'POST':
        form = DrugForm(request.POST)
        if form.is_valid():
            drug = form.save(commit=False)
            drug.patient = result.patient
            drug.save()
            # Redirect to the same page to avoid form resubmission
            return redirect('prescribe_drug', result_id=result_id)

    else:
        form = DrugForm()

    context = {
        "result": result,
        "form": form,
        "pres": pres
    }
    return render(request, 'pharmacy/index.html', context)




def drug_stock(request):
    return render(request,'pharmacy/stock.html' )