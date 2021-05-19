from django.db.models.fields.related import ManyToManyField
from django.shortcuts import render, HttpResponse
import calendar
from .models import Month, Day
import json

def index(request):
    yearCalender = calendar.HTMLCalendar().formatyear(2021)

    context = {
        'YC': yearCalender,
        # 'month_list': month_list,    
    }
    
    return render(request, 'main.html', context)


def viewSeat(request):
    month_list = Month.objects.all()
    dateDay = request.POST.get('dateDay')

    resSeat = 0
    for ml in month_list:
        for dl in ml.day_set.all():
            if dl.day == dateDay: 
                resSeat = dl.remain_seat 
            
    yearCalender = calendar.HTMLCalendar().formatyear(2021)
    context = {  
        'resSeat': resSeat,    
    }
    return HttpResponse(json.dumps(context), content_type="application/json")


def checkSeat(request):
    month_list = Month.objects.all()
    reqDay = request.POST.get('reqDay')
    conCheck = request.POST.get('conCheck')

    resSeat = 0
    if conCheck == "purchase":
        for ml in month_list:
            for dl in ml.day_set.all():
                if dl.day == reqDay: 
                    dl.remain_seat -= 1
                    dl.save()
                    resSeat = dl.remain_seat
    elif conCheck == "cancel":
        for ml in month_list:
            for dl in ml.day_set.all():
                if dl.day == reqDay: 
                    dl.remain_seat += 1
                    dl.save()
                    resSeat = dl.remain_seat
    
    yearCalender = calendar.HTMLCalendar().formatyear(2021)
    context = {  
        'resSeat': resSeat,    
    }
    return HttpResponse(json.dumps(context), content_type="application/json")




dayMax = 32
def saveData(request):
    global dayMax
    month_list = Month.objects.all()
    for ml in month_list:
        if ml.month == 'May':
            dayMax = 32
        elif ml.month == 'June':
            dayMax = 31
        elif ml.month == 'July':
            dayMax = 32
        elif ml.month == 'August':
            dayMax = 32
        for i in range(1, dayMax):
            varDay = Day()
            varDay.day = i
            varDay.remain_seat = 4
            varDay.f_month = ml
            varDay.save()
    return render(request, 'main.html')
