from django.shortcuts import render,HttpResponse

def ALL(request):
    return render(request, 'cv/ALL')

def profil_umum(request):
    return render(request, 'cv/profil_umum.html')

def informasi_kontak(request):
    return render(request, 'cv/informasi_kontak.html')

def kemampuan(request):
    return render(request, 'cv/kemampuan.html')   

def pendidikan(request):
    return render(request, 'cv/pendidikan.html')

def pengalaman(request):
    return render(request, 'cv/pengalaman.html')