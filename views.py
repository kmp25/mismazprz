from django.shortcuts import render

# Create your views here.
from .models import Podmiot



def lista(request):
    return render(request,'mmp/index.html',{
        'Podmiot':Podmiot.objects.all()
    })