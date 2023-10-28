from django.http import HttpResponseBadRequest
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from patients.forms import PatientRegistrationForm
from patients.models import Patient, Result, Test
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
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


@login_required
def view_patient(request, mrn):
    patient = get_object_or_404(Patient,medical_record_number=mrn)
    
    results = Result.objects.select_related('patient','test').filter(patient=patient)
    referring_url = request.META.get('HTTP_REFERER', '/')

    if request.method == 'POST':
        test_id = request.POST.get('test')
        result = request.POST.get('result')
        comment = request.POST.get('comment')

        try:
            test = Test.objects.get(id=test_id)
        except Test.DoesNotExist:
            return HttpResponseBadRequest("Invalid test ID")

        test_result, created = Result.objects.get_or_create(patient=patient, test=test, done=False)
        test_result.results = result
        test_result.comment = comment
        test_result.date = timezone.now()
        test_result.done = True
        test_result.done_by = request.user
        test_result.save()
        return redirect(referring_url)

    context = {
        'patient': patient,
        'results': results,
    }

    return render(request, 'patients/results.html', context)




@login_required
def view_results(request,test_id,patient_id):
    test=Test.objects.get(id=test_id)
    patient=get_object_or_404(Patient,id=patient_id)
    results=get_object_or_404(Result,test=test,patient=patient)
    context={
        'results':results
    }
    return render(request,'patients/view.html',context)



class PatientListView(ListView):
    model = Patient
    template_name = 'patients/index.html'
    context_object_name = 'patients'
    paginate_by = 4 

    def get_template_names(self):
        if self.request.htmx:
            return 'patients/patient-list.html'
        return 'patients/index.html'
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['results'] = Result.objects.all()
        context['patients_num']=Patient.objects.all().count()
        return context
