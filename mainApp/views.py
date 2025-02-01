from django.shortcuts import render,redirect
from .models import *

def home_view(request):
    return render(request, 'index.html')

def fanlar_view(request):
    fanlar = Fan.objects.all()
    context = {
        'fanlar': fanlar,
    }
    return render(request, 'fanlar.html', context)

def yonalishlar_view(request):
    yonalishlar = Yonalish.objects.all()
    context = {
        'yonalishlar': yonalishlar,
    }
    return render(request, 'yonalishlar.html', context)

def ustozlar_view(request):
    ustozlar = Ustoz.objects.all()
    context = {
        'ustozlar': ustozlar,
    }
    return render(request, 'ustozlar.html', context)

def yonalish_qoshish_view(request):
    if request.method == "POST":
        Yonalish.objects.create(
            nom=request.POST.get('nom'),
            aktiv=request.POST.get('aktiv') == 'on',
        )
        return redirect("/yonalishlar/")
    return render(request,"yonalish_qoshish.html")

def fanlar_qoshish_view(request):
    if request.method == "POST":
        yonalish_id = request.POST.get('yonalish')


        if yonalish_id != 'None':
            yonalish = Yonalish.objects.get(id=yonalish_id)
        else:
            yonalish=None
        Fan.objects.create(
            nom=request.POST.get('nom'),
            asosiy=request.POST.get('asosiy') == 'on',
            yonalish=yonalish,

        )
        return redirect("/fanlar/")
    yonalish = Yonalish.objects.all()
    context={
        "yonalish":yonalish,
    }
    return render(request,"fanlar_qoshish.html", context)

def ustoz_qoshish_view(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        jins = request.POST.get('jins')
        yosh = request.POST.get('yosh')
        daraja = request.POST.get('daraja')
        fan_id = request.POST.get('fan')


        fan = None
        if fan_id != 'None':
            fan = Fan.objects.get(id=fan_id)


        Ustoz.objects.create(
            nom=nom,
            jins=jins,
            yosh=yosh,
            daraja=daraja,
            fan=fan
        )

        return redirect("/ustozlar/")

    fanlar = Fan.objects.all()
    context = {
        "fanlar": fanlar,
    }

    return render(request, "ustozlar_qoshish.html", context)

