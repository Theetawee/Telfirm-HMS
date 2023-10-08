from django.utils import timezone
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login,logout
from .forms import PatientRegistrationForm,ResultForm
from .models import Patient,Test,Results


def login_view(request):
    referring_url = request.META.get('HTTP_REFERER', '/')

    if request.user.is_authenticated:
        # Redirect authenticated users to the referring URL
        return redirect(referring_url)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Log the user in
            auth_login(request, form.get_user())
            # Redirect to the referring URL (or a default URL)
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    # If there are errors, the form will contain error messages
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')



def new_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the patient data
            form.save()
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
        form = ResultForm(request.POST)
        test = Test.objects.get(id=request.POST['test'])
        if form.is_valid():
            t_results = form.save(commit=False)
            t_results.done_by = request.user
            t_results.patient = patient
            t_results.test = test
            t_results.save()
            return redirect('home')
    else:
        form = ResultForm()

    context = {
        'patient': patient,
        'form': form,
        'results': results
    }

    return render(request, 'accounts/patient/results.html', context)
