from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.http import HttpResponse


# Create your views here.
def login(request):
    if request.session.has_key('user'):
        studmail = request.session['user']
        stud = Student.objects.get(email=studmail)
        return redirect('/')

    elif request.method =='POST':
        studmail = request.POST.get('email','')
        studpass = request.POST.get('pass','')
        if (Student.objects.filter(email=studmail, password=studpass).exists()):
            request.session['user']= studmail
            return redirect('/')
        else:
            return HttpResponse("<script>alert('Either Email or Password is incorrect')</script>")
    return render(request, 'csdata/login.html')

def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return redirect('/')

def register(request):
    if request.method =='POST':
        name=request.POST.get('rname','')
        email=request.POST.get('remail','')
        rollno=request.POST.get('rollno','')
        passwrd=request.POST.get('rpass','')
        if Student.objects.filter(email=email).exists():
            return HttpResponse("<script>alert('This Email already exist')</script>")
        else:
            stud = Student(name=name, email=email, rollno=rollno, password=passwrd)
            stud.save()
            request.session['user']= email
            return redirect('/')
    return render(request, 'csdata/login.html')

def notes(request):
    if request.session.has_key('user'):
        return render(request, 'csdata/notesl.html')
    return redirect('/data/login/')

def pdfbooks(request):
    if request.session.has_key('user'):
        return render(request, 'csdata/pdfbooks.html')
    return redirect('/data/login/')

def syllabus(request):
    if request.session.has_key('user'):
        return redirect('https://drive.google.com/folderview?id=1PJeHhTB1lqO5losmQdHBo2IVhg_7vYZF')
    return redirect('/data/login/')

def prevppr(request):
    if request.session.has_key('user'):
        return redirect('https://drive.google.com/folderview?id=1-D8l9szcU89H_ImqnnZDSanGWGL9NVWY')
    return redirect('/data/login/')