from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Broadcast

def search_form(request):
    return render_to_response('search-form.html')

def search(request):
    broadcast =[]
    try:
        s = request.GET['s']
        broadcast = Broadcast.objects.filter(name=s)
    except:
        s = 'Ничего не найдено'
    return render_to_response('search.html', {'s':s, 'broadcast':broadcast})
