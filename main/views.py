from django.shortcuts import render
import calendar

def index(request):
    yearCalender = calendar.HTMLCalendar().formatyear(2021)
    context = {'YC': yearCalender,}
    return render(request, 'main.html', context)

