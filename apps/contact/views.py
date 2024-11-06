from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        web_site = request.POST.get('web_site')
        phone_number = request.POST.get('phone_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and phone_number:
            contact = Contact.objects.create(
                user_id=request.user.id,
                name=name,
                email=email,
                web_site=web_site,
                phone_number=phone_number,
                subject=subject,
                message=message
            )
            contact.save()
            messages.success(request, 'Sizning xabaringiz muvaffaqiyatli yuborildi.')
            return redirect('contact')
        else:
            messages.error(request, 'Iltimos, barcha maydonlarni to\'ldiring.')
    
    return render(request, 'contact.html')