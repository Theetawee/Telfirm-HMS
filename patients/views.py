from django.http import HttpResponseBadRequest
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from patients.forms import PatientRegistrationForm
from patients.models import Patient, Result, Test
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
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
    patient = get_object_or_404(Patient, mrn=mrn)
    results = Result.objects.select_related("patient", "test").filter(patient=patient)
    context = {
        "patient": patient,
        "results": results,
    }

    return render(request, "patients/view.html", context)


@login_required
def view_results(request, test_id, patient_id):
    test = Test.objects.get(id=test_id)
    patient = get_object_or_404(Patient, id=patient_id)
    result = get_object_or_404(Result, test=test, patient=patient)
    if request.POST:
        rapid_tr=request.POST.get('rapid_tr')
        standard_tr=request.POST.get('standard_tr')
        other_comments=request.POST.get('other_comments')
        result.rapid_tr=rapid_tr
        result.standard_tr=standard_tr
        result.comment=other_comments
        result.done_by=request.user
        result.date=timezone.now()
        result.done=True
        result.save()
        messages.success(request,'Results added successfully')
        return redirect('view',mrn=patient.mrn)
    context = {"result": result,'patient':patient}
    return render(request, "patients/result.html", context)


class PatientListView(ListView):
    model = Patient
    template_name = "patients/index.html"
    context_object_name = "patients"
    paginate_by = 4

    def get_template_names(self):
        if self.request.htmx:
            return "patients/patient-list.html"
        return "patients/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["results"] = Result.objects.all()
        context["patients_num"] = Patient.objects.all().count()
        return context


def patientsList(request):
    patients = Patient.objects.all()[:1]
    context = {"patients": patients}
    return render(request, "patients/index.html", context)


def load_p(request):
    print("yes")
    patients = Patient.objects.all()
    p = Paginator(patients, 1)
    page = request.GET.get("page", 1)
    patients_list = p.get_page(page)
    context = {"patients": patients_list}
    return render(request, "main/list.html", context)
