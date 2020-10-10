from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from csdata.models import Contact
from django.core.mail import send_mail
from csnexus.settings import EMAIL_HOST_USER

def home(request):
    if request.session.has_key('user'):
        return render(request,'Index.html',{'login':True})
    return render(request,'Index.html', {'login':False})

def contact(request):
    if request.method == 'POST':
        name= request.POST.get('contactname','')
        rn= request.POST.get('rollno','')
        email= request.POST.get('contactemail','')
        message = request.POST.get('contactmsg','')
        contact = Contact(cname=name, cemail=email, crollno= rn, msg=message)
        contact.save()
        subject = 'Message From ' + str(email)
        message = str(name) + ":\n"+ message + "\n" + str(rn)
        recepient = 'csnexus76@gmail.com'
        send_mail(subject, 
             message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return redirect('/')