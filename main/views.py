from django.shortcuts import render
import json
# Create your views here.

def home(request):
    return render(request, 'main/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        data = {
            'name': name,
            'phone': phone,
            'message': message
        }

        with open('contacts.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)
    return render(request, 'main/contacts.html')
