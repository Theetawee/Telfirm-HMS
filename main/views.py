from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from accounts.models import Patient
from django.db.models import Q


@login_required
def index(request):
    return render(request, "main/index.html")


def search(request):
    patient = request.GET.get('patient').upper()
    if patient is None:
        return redirect('home')
    else:
        patient_qs = Patient.objects.filter(
            Q(medical_record_number__exact=patient) |
            Q(first_name__icontains=patient) |
            Q(last_name__icontains=patient)
        )
        context={
            'qs':patient_qs
        }
    return render(request, 'main/search.html', context)


def docs(request):
    return render(request,'main/docs.html' )