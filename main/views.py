from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from django.core.paginator import Paginator
from patients.models import Patient
from django.db.models import Count
from .forms import CreateNoticeForm
from django.contrib import messages
from .models import Notice
from django.contrib.auth.decorators import login_required

@login_required
def search(request):
    patient = request.POST.get("patient").upper()
    af = True
    patient_qs = Patient.objects.filter(
        Q(mrn__exact=patient)
        | Q(first_name__icontains=patient)
        | Q(last_name__icontains=patient)
    )
    context = {"patients": patient_qs, "autofocus": af}
    return render(request, "main/search.html", context)

@login_required
def create_notice(request):
    if request.POST:
        form = CreateNoticeForm(request.POST)
        if form.is_valid():
            notice = form.save()
            notice.author = request.user
            notice.save()
            messages.success(request, "Notice created successfully")
            return redirect("dashboard")
    form = CreateNoticeForm()
    context = {"form": form}
    return render(request, "main/create_notice.html", context)

@login_required
def view_notice(request):
    url = request.META.get("HTTP_REFERER")
    notices = Notice.objects.all()
    context = {"notices": notices, "url": url}
    return render(request, "main/notice.html", context)

@login_required
def view_notice_detail(request, pk):
    notice = Notice.objects.get(id=pk)
    context = {"notice": notice}
    return render(request, "main/content.html", context)
@login_required
def close_notice(request,pk):
    notice=Notice.objects.get(id=pk)
    context={"notice":notice}
    return render(request, "main/close.html",context)



@login_required
def mark_read(request,pk):
    notice=Notice.objects.get(id=pk)
    notice.read_by.add(request.user)
    notice.save()
    return HttpResponse("marked as read")