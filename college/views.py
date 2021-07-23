from django.shortcuts import render
from datetime import datetime
from college.models import db
from django.contrib import messages


# Create your views here.
def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=db(name=name,email=email,phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.add_message(request, messages.INFO, 'your message has been sent!')

    return render(request,'index.html')