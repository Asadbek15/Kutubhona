
from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import *
def Salomlash(request):
    return render( request,"salomlash.html")

def Men(request):
     return render( request,"men.html")

def Loiha(request):
    return render(request, "loiha.html")

def asosiy(request):
    return render(request, "asosiy.html")


def mualliflar(request):
    m = Muallif.objects.all().order_by("ism")
    return render(request, "avtor.html", {"a": m})


def kitob_delete(request, son):
    Kitob.objects.get(id=son).order_by("nom")
    return redirect("/kitob/")












# 2-qisim
# 1
def k_muallif(request):
    muallif=Muallif.objects.all()
    if request.method == 'POST':
        if request.POST.get("t")=="False":
            natija=False
        else:
            natija=True
        Muallif.objects.create(
            ism=request.POST.get("ism"),
            tirik=natija,
            yosh=request.POST.get("y"),
            kitoblar_soni=request.POST.get("k_s"),
        )
        return redirect("/muallif/")
    return render(request,"muallif.html",{"t": muallif})


def kitob(request):
    n = Kitob.objects.all()
    b=Muallif.objects.all()
    if request.method == "POST":
        m = request.POST.get("m")
        muallif = Muallif.objects.get(id=m)
        Kitob.objects.create(
            nom=request.POST.get("nom"),
            sana=request.POST.get("s"),
            sahifa=request.POST.get("s_h"),
            janr=request.POST.get("j"),
            muallif=muallif,
        )
        return redirect("/books/")
    return render(request,"books.html",{"books":n,"avtor":b})



def student(request):
    f = Student.objects.all()
    if request.method == 'POST':
        if request.POST.get("a")=="False":
            natija=False
        else:
            natija=True
    Student.objects.create(


    )

    return render(request,"student.html",{"k1":f})

def kitob_edit(request, pk):
    if request.method == "POST":
        f1=Kitob.objects.get(id=pk)
        f1.nom=request.POST.get("nom"),
        f1.sana=request.POST.get("s"),
        f1.sahifa=request.POST.get("s_h"),
        f1.janr=request.POST.get("j"),
        f1.muallif=request.POST.get("m_f"),
        f1.save()
        return redirect("/books/")
    m=Kitob.objects.get(id=pk)
    return render(request,"books.html",{"kitoblar":m})


def record(request,pk):
    m=Record.objects.get(id=pk)