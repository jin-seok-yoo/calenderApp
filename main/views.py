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




count = 1
def saveData(request):
    global count
    if count == 32:
        return render(request, 'main.html')
    else:
        month_list = Month.objects.all()
        
        varMonth = Month()
        varDay = Day()
        
        for ml in month_list:
            varDay.day = count
            varDay.remain_seat = 4
            varDay.f_month = ml
            varDay.save()
        count += 1
        return saveData(request)