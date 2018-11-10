from django.shortcuts import render
from django.http import HttpResponse
import operator


# Create your views here.
def home(request):
    return render(request, 'home.html')

def licznik(request):
    slowa = request.GET['slowa']
    wyrazy = slowa.split()

    slownik = {}

    for wyraz in wyrazy:
        if wyraz in slownik:
            slownik[wyraz] += 1
        else:
            slownik[wyraz] = 1

    posortowane = sorted(slownik.items(), key=operator.itemgetter(1), reverse=True)


    return render(request, 'licznik.html', {'slowa':len(slowa), 'wyrazy':len(wyrazy), 'posortowane':posortowane})



def about(request):
        return render(request, 'about.html')
