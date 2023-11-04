from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from patients.models import Patient,Result


def index(request):
    if not request.user.is_authenticated:
        return render(request,'main/intro.html')
    else:
        patients_list=Patient.objects.all()
        p=Paginator(patients_list,1)
        page=int(request.GET.get('page',1))
        patients=p.get_page(page)
        results=Result.objects.all()
        context={
            'patients':patients,
            'results':results
        }
    return render(request, "main/index.html",context)


def intro(request):
    return render(request,'main/intro.html' )


def search(request):
    patient = request.POST.get('patient').upper()
    
    patient_qs = Patient.objects.filter(
        Q(medical_record_number__exact=patient) |
        Q(first_name__icontains=patient) |
        Q(last_name__icontains=patient)
    )
    context={
        'patients':patient_qs
    }
    return render(request, 'main/search.html', context)


def get_pending(request):
    patients=Patient.objects.all()
    context={
        'patients':patients
    }
    return render(request,'main/pending.htmx.html',context)



def get_done(request):
    patients=Patient.objects.all()
    context={
        'patients':patients
    }
    return render(request,'main/done.htmx.html',context)


def get_all(request):
    patients=Patient.objects.all()
    context={
        'patients':patients
    }
    return render(request,'main/all.htmx.html',context)




def docs(request):
    return render(request,'main/docs.html' )