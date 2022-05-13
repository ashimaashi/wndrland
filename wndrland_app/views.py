from django.shortcuts import render, redirect
from .models import Subscriber_newsletter,contact_us

# Create your views here.
def home(request):
    if request.method == 'POST':
        email = request.POST['email']
        new_subscriber = Subscriber_newsletter(email=email)
        new_subscriber.save()
        return redirect('home')
    return render(request, 'home.html')

def about(request):
    return render(request, 'roadmap.html')

def vision(request):
    return render(request, 'our-vision.html')

def contact(request):
    if request.method == 'POST':
        print(request.POST.values)
        email = request.POST['email']
        fname = request.POST['fname']
        phone = request.POST['phone']
        address = request.POST['address']
        review = request.POST['review']
        new_contact = contact_us(name=fname,email=email, address=address , phone=phone, review=review)
        new_contact.save()
        return redirect('contact')

    return render(request, 'contact.html')