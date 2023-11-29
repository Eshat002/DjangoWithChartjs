 # charts/views.py
from django.shortcuts import render
from .models import RichPerson
from django.http import JsonResponse,HttpResponse


def rich_people_chart(request):
    return render(request, "rich_person.html")


def get_data(request):
    rich_people = RichPerson.objects.all()
    
    data = []
    for rich_person in rich_people:
        item = {
         
            'name': rich_person.name,
            'wealth': rich_person.wealth
        }
        data.append(item)

    return JsonResponse({"data":data})
   

