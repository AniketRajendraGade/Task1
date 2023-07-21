from django.shortcuts import render,redirect
from .forms import user
from .models import Task
from django.core.mail import send_mail



# Create your views here.
def addUser(request):
    if request.method == 'POST':
        form = user(request.POST)
        if form.is_valid():
            form.save()
            subject = 'Registration Successful!!'
            message = 'Thank you for your intrest'
            sender = "aniketgade04@gmail.com"
            rec = [form.cleaned_data['email']]

            send_mail(subject, message, sender, rec)

            return redirect('/all') 
    else:
        form = user()

        

    return render(request, 'index.html', {'form': form})

def all(request):
    users = Task.objects.all()
    return render(request, 'all.html', {'users': users})

