from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Attorneys
from .filters import AttorneyFilter

def home(request):
    return render(request, 'legally/home.html')

def services(request):
    return render(request, 'legally/services.html')

@login_required
def appointment(request):
    return render(request, 'legally/appointment.html')

@login_required
def attorneys(request):
    attorney_list =Attorneys.objects.all()
    attorney_filter = AttorneyFilter(request.GET, queryset=attorney_list)
    return render(request, 'legally/attorneys.html',
    {'attorney_list': attorney_list,
    'attorney_filter': attorney_filter})

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        results = Attorneys.objects.filter(speciality__s_name__contains=searched)
        return render(request, 'legally/search.html',
        {'searched': searched,
        'results': results})
    else:
        return render(request, 'legally/search.html')

def filter(request):
    attorney_list = Attorneys.objects.all()
    attorney_filter = AttorneyFilter(request.GET, queryset=attorney_list)
    return render(request, 'legally/filter.html',
    {'attorney_filter': attorney_filter})