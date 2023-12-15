from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from patients.forms import PatientRegistrationForm
from patients.models import Patient, Result, Test
from django.contrib.auth.decorators import login_required
from .utils import create_mrn

# Create your views here.


@login_required
def new_patient(request):
    if request.method == "POST":
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            p = form.save()
            p.mrn = create_mrn()
            p.save()
            for test in p.tests.all():
                Result.objects.create(patient=p, test=test).save()
            messages.success(
                request,
                f"Patient successfully registered. Medical Record Number(MRN): {p.mrn}",
            )
            return redirect("dashboard")
        else:
            # If there are errors, render the form with errors
            context = {"form": form}
            return render(request, "accounts/patient/new.html", context)
    else:
        # For GET requests, display an empty form
        form = PatientRegistrationForm()
        context = {"form": form}
        return render(request, "patients/new.html", context)


@login_required
def view_patient(request, mrn):
    patient=Patient.objects.prefetch_related("tests").get(mrn=mrn)
    results = Result.objects.select_related("patient", "test").filter(patient=patient)
    context = {
        "patient": patient,
        "results": results,
    }

    return render(request, "patients/view.html", context)


@login_required
def view_results(request, test_id, patient_id):
    test = Test.objects.get(id=test_id)
    patient=Patient.objects.prefetch_related("tests").get(id=patient_id)
    result=Result.objects.select_related("patient","test").get(test=test,patient=patient)
    if request.POST:
        rapid_tr = request.POST.get("rapid_tr")
        standard_tr = request.POST.get("standard_tr")
        other_comments = request.POST.get("other_comments")
        result.rapid_tr = rapid_tr
        result.standard_tr = standard_tr
        result.comment = other_comments
        result.done_by = request.user
        result.date = timezone.now()
        result.done = True
        result.save()
        messages.success(request, "Results added successfully")
        return redirect("view", mrn=patient.mrn)
    context = {"result": result, "patient": patient}
    return render(request, "patients/result.html", context)

@login_required
def see_results(request, test_id, patient_id):
    patient=Patient.objects.prefetch_related("tests").get(id=patient_id)
    test = get_object_or_404(Test, id=test_id)
    result=Result.objects.select_related("patient","test").get(test=test,patient=patient)
    rapid_tr_value = result.rapid_tr
    standard_tr_value = result.standard_tr
    comment_value = result.comment
    context = {
        "rapid_tr_value": rapid_tr_value,
        "standard_tr_value": standard_tr_value,
        "comment_value": comment_value,
        "patient": patient,
        "result": result,
    }
    return render(request, "patients/edit_results.html", context)

@login_required
def confirm_results(request, test_id, patient_id):
    patient=Patient.objects.prefetch_related("tests").get(id=patient_id)
    test = get_object_or_404(Test, id=test_id)
    result=Result.objects.select_related("patient","test").get(test=test,patient=patient)
    result.confirmed = True
    result.save()
    messages.success(request, "Results confirmed successfully")
    return redirect("view", mrn=patient.mrn)

@login_required
def print_results(request, test_id, patient_id):
    patient=Patient.objects.prefetch_related("tests").get(id=patient_id)
    test = get_object_or_404(Test, id=test_id)
    result=Result.objects.select_related("patient","test","done_by").get(test=test,patient=patient)
    rapid_tr_value = result.rapid_tr
    standard_tr_value = result.standard_tr
    comment_value = result.comment
    context = {
        "rapid_tr_value": rapid_tr_value,
        "standard_tr_value": standard_tr_value,
        "comment_value": comment_value,
        "patient": patient,
        "result": result,
    }
    return render(request, "patients/print.html", context)
