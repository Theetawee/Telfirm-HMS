from datetime import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from patients.forms import PatientRegistrationForm
from patients.models import Patient, Result, Test

# Create your views here.

def new_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            p=form.save()
            for test in p.tests.all():
                Result.objects.create(patient=p,test=test).save()
            # Redirect to a success page or another appropriate URL
            messages.success(request,f'Patient successfully registered. Medical Record Number(MRN): {p.medical_record_number}')
            return redirect('patient_mgt')
        else:
            # If there are errors, render the form with errors
            context = {'form': form}
            return render(request, 'accounts/patient/new.html', context)
    else:
        # For GET requests, display an empty form
        form = PatientRegistrationForm()
        context = {'form': form}
        return render(request, 'patients/new.html', context)


def results(request, mrn):
    patient = get_object_or_404(Patient, medical_record_number=mrn)
    results = Result.objects.filter(patient=patient)

    if request.method == 'POST':
        test_id=request.POST['test']
        result=request.POST.get('result')
        comment=request.POST.get('comment')
        test=Test.objects.get(id=test_id)
        test_result=Result.objects.get(patient=patient,test=test,done=False)
        test_result.results=result
        test_result.comment=comment
        test_result.date=timezone.now()
        test_result.done=True
        test_result.done_by=request.user
        test_result.save()
        return redirect('home')
    context = {
        'patient': patient,
        'results': results
    }

    return render(request, 'patients/results.html', context)


def view_results(request,test_id,patient_id):
    test=Test.objects.get(id=test_id)
    patient=get_object_or_404(Patient,id=patient_id)
    results=get_object_or_404(Result,test=test,patient=patient)
    context={
        'results':results
    }
    return render(request,'patients/view.html',context)



def patient_mgt(request):
    patients=Patient.objects.all()
    results=Result.objects.all()
    context={
        'patients':patients,
        'results':results
    }
    return render(request,'patients/index.html',context )