from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from patients.models import Patient, Result
from django.db.models import Count

# Create your views here.


def dashboard_view(request):
    patients=Patient.objects.all().count()
    context={'total_patients':patients}
    return render(request, "dashboard/index.html",context)


def search_view(request):
    patient = request.POST.get("patient").upper()

    patient_qs = Patient.objects.filter(
        Q(mrn__exact=patient)
        | Q(first_name__icontains=patient)
        | Q(last_name__icontains=patient)
    )
    context = {"patients": patient_qs}
    return render(request, "main/search.html", context)


def load_patients(request):
    patients_list = Patient.objects.all()
    p = Paginator(patients_list, 2)
    page = int(request.GET.get("page", 1))
    patients = p.get_page(page)
    context = {"patients": patients, "patients_num": patients_list.count()}
    return render(request, "dashboard/htmx/patients_load.html", context)
