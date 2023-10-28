from django.shortcuts import get_object_or_404, redirect, render
from patients.models import  Result,Patient
from .models import Prescription
from .forms import DrugForm
from django.contrib.auth.decorators import login_required
# Create your views here.




@login_required
def drug_stock(request):
    return render(request,'pharmacy/stock.html' )