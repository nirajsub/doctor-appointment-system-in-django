
from django.shortcuts import render
from django.contrib import messages
from pages.models import Contact


def contact_page(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        address = request.POST['address']
        print(name, email, phone, content, address)

        if len(name) < 2 or len(email) < 3 or len(phone) < 5 or len(content) < 3:
            messages.error(request, 'please fill the form correctly')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Your messege is sucessfully submitted')
    return render(request, "contact.html", {})

def about_page(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "about.html", {})

def news_page(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "news.html", {})