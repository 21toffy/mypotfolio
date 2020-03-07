from django.shortcuts import render, redirect
from .models import Services, About_Me
from jobs.models import Job

from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from django.core.mail import send_mail


def home(request):
    serviceo = Services.objects.all()
    about = About_Me.objects.all()[:1]
    job = Job.objects.all()
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message="{0} has sent you a new message:\n\n{1}".format(email, forms.cleaned_data[message])
            send_mail=('NEW Enquiry', message, subject, ['oketofoke@gmail.com'])
            return HttpResponse('success thank you for your message.')
    else:
        form = ContactForm()
    context= {'serviceo':serviceo, 'about':about, 'job':job, 'form':form}
    return render(request, 'others/home.html', context)
    pass

def contact(request):
    pass

def services(request):
    service = services.objects.all()
    return render(request, 'others/home.html', service)

def about(request):
    about = About_Me.objects.all()
    return render(request, 'others/home.html', about)


# def emailView(request):
#     if request.method=='GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             try: 
#                 send_mail(subject, message, email, ['admin@example.com'])
#             except BadHeaderError:

#                 return HttpResponse('Invalid header found.')
#             return redirect('others:success')
#     return render(request, 'others/email.html', {'form':form})



            

def emailView(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message="{0} has sent you a new message:\n\n{1}".format(email, forms.cleaned_data[message])
            send_mail=('NEW Enquiry', message, subject, ['oketofoke@gmail.com'])
            return HttpResponse('success thank you for your message.')
    else:
        form = ContactForm()

    
    return render(request, 'others/email.html', {'form':form})

def successView(request):
    return HttpResponse('success thank you for your message.')


def security(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message="{0} has sent you a new message:\n\n{1}".format(email, forms.cleaned_data[message])
            send_mail=('NEW Enquiry', message, subject, ['oketofoke@gmail.com'])
            return HttpResponse('success thank you for your message.')
    else:
        form = ContactForm()
    return render(request, 'others/security.html', {'form':form})


def seo_optimization(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message="{0} has sent you a new message:\n\n{1}".format(email, forms.cleaned_data[message])
            send_mail=('NEW Enquiry', message, subject, ['oketofoke@gmail.com'])
            return HttpResponse('success thank you for your message.')
    else:
        form = ContactForm()
    return render(request, 'others/seo_optimization.html', {'form':form})


def cloud(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message="{0} has sent you a new message:\n\n{1}".format(email, forms.cleaned_data[message])
            send_mail=('NEW Enquiry', message, subject, ['oketofoke@gmail.com'])
            return HttpResponse('success thank you for your message.')
    else:
        form = ContactForm()
    return render(request, 'others/cloud.html', {'form':form})


def maintenance(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message="{0} has sent you a new message:\n\n{1}".format(email, forms.cleaned_data[message])
            send_mail=('NEW Enquiry', message, subject, ['oketofoke@gmail.com'])
            return HttpResponse('success thank you for your message.')
    else:
        form = ContactForm()
    return render(request, 'others/maintenance.html', {'form':form})



from django.shortcuts import render

# def handler404(request):
#     return render(request, 'others/404.html', status=404)


# def handler500(request):
#     return render(request, 'others/500.html', status=500)
