from django.shortcuts import render
import calendar
from .models import Month, Day

def index(request):
    month_list = Month.objects.all()
    
    yearCalender = calendar.HTMLCalendar().formatyear(2021)

    context = {
        'YC': yearCalender,
        'month_list': month_list,    
    }
    
    return render(request, 'main.html', context)

def saveForm(request):
    test = [
        {1, 2},
        {3, 4}
    ]
    context = {'test': test,}
    return render(request, 'main.html', context)