from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from patients.models import Patient, Result
from django.db.models import Count
from django.conf import settings

# Create your views here.

@login_required
def dashboard_view(request):
    patients = Patient.objects.all().count()
    context = {"total_patients": patients}
    return render(request, "dashboard/index.html", context)

@login_required
def search_view(request):
    patient = request.POST.get("patient").upper()

    patient_qs = Patient.objects.filter(
        Q(mrn__exact=patient)
        | Q(first_name__icontains=patient)
        | Q(last_name__icontains=patient)
    )
    context = {"patients": patient_qs}
    return render(request, "main/search.html", context)

@login_required
def load_patients(request):
    context = {}
    patients_list = Patient.objects.all()

    # Handle pagination
    try:
        page = request.GET.get("page", 1)
        paginator = Paginator(patients_list, settings.ENTRIES_PER_PAGE)
        patients = paginator.get_page(page)
        context["patients"] = patients
    except EmptyPage:
        # If the requested page is out of range, deliver an empty page
        context["patients"] = Paginator([], 1).get_page(1)

    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        context["patients"] = paginator.get_page(1)

    return render(request, "dashboard/htmx/patients_load.html", context)

@login_required
def load_patients_page(request):
    context = {}
    patients_list = Patient.objects.all()

    # Handle pagination
    try:
        page = request.GET.get("page", 1)
        paginator = Paginator(patients_list, settings.ENTRIES_PER_PAGE)
        patients = paginator.get_page(page)
        context["patients"] = patients
    except EmptyPage:
        # If the requested page is out of range, deliver an empty page
        context["patients"] = Paginator([], 1).get_page(1)

    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        context["patients"] = paginator.get_page(1)

    return render(request, "dashboard/htmx/patients.html", context)
