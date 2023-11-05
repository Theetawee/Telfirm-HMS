from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from patients.models import Patient,Result
from django.db.models import Count


def index(request):
    if not request.user.is_authenticated:
        return render(request,'main/intro.html')
    else:
        patients_list=Patient.objects.all()
        p=Paginator(patients_list,10)
        page=int(request.GET.get('page',1))
        patients=p.get_page(page)
        context={
            'patients':patients,
            'patients_num':patients_list.count()
        }
    return render(request, "main/index.html",context)


def load_more(request):
    patients_list=Patient.objects.all()
    p=Paginator(patients_list,10)
    page=int(request.GET.get('page',1))
    patients=p.get_page(page)
    context={
        'patients':patients,
    }
    return render(request, "main/sect.htmx.html",context)



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
    patients_with_undone_results = Patient.objects.annotate(
        undone_result_count=Count('result', filter=Q(result__done=False))
    ).filter(undone_result_count__gt=0)

    p = Paginator(patients_with_undone_results, 10)
    page = int(request.GET.get('page', 1))
    patients = p.get_page(page)

    context = {
        'patients': patients
    }
    return render(request, 'main/pending.htmx.html', context)


def get_done(request):
    patients_with_done_results = Patient.objects.annotate(
        done_result_count=Count('result', filter=Q(result__done=True))
    ).filter(done_result_count__gt=0)

    p = Paginator(patients_with_done_results, 10)
    page = int(request.GET.get('page', 1))
    patients = p.get_page(page)

    context = {
        'patients': patients
    }
    return render(request, 'main/done.htmx.html', context)





def get_all(request):
    patients_list=Patient.objects.all()
    p=Paginator(patients_list,10)
    page=int(request.GET.get('page',1))
    patients=p.get_page(page)
    
    context={
        'patients':patients
    }
    return render(request,'main/all.htmx.html',context)




def docs(request):
    return render(request,'main/docs.html' )