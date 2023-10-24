from datetime import timezone
from django.shortcuts import get_object_or_404, redirect, render

from patients.forms import PatientRegistrationForm
from patients.models import Patient, Results, Test

# Create your views here.

def new_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            p=form.save()
            for test in p.tests.all():
                Results.objects.create(patient=p,test=test).save()
            # Redirect to a success page or another appropriate URL
            return redirect('home')
        else:
            # If there are errors, render the form with errors
            context = {'form': form}
            return render(request, 'accounts/patient/new.html', context)
    else:
        # For GET requests, display an empty form
        form = PatientRegistrationForm()
        context = {'form': form}
        return render(request, 'accounts/patient/new.html', context)


def results(request, mrn):
    patient = get_object_or_404(Patient, medical_record_number=mrn)
    results = Results.objects.filter(patient=patient)

    if request.method == 'POST':
        test_id=request.POST['test']
        result=request.POST.get('result')
        comment=request.POST.get('comment')
        test=Test.objects.get(id=test_id)
        test_result=Results.objects.get(patient=patient,test=test,done=False)
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

    return render(request, 'accounts/patient/results.html', context)


def view_results(request,test_id,patient_id):
    test=Test.objects.get(id=test_id)
    patient=get_object_or_404(Patient,id=patient_id)
    results=get_object_or_404(Results,test=test,patient=patient)
    context={
        'results':results
    }
    return render(request,'accounts/patient/view.html',context)



def patient_mgt(request):
    patients=Patient.objects.all()
    context={
        'patients':patients
    }
    return render(request,'patients/index.html',context )