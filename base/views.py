from django.shortcuts import render

from .models import Info

def landing(request):

    c = {}

    c['logged_in'] = request.user.is_authenticated

    print(c['logged_in'])

    return render(request, 'landing.html', c)

def contact(request):

    return render(request, 'contact.html')

def plans(request):

    return render(request, 'plans.html')

# Info
def terms(request):

    return render(request, 'info/terms.html', {'info': Info.objects.get(title = 'Договор-оферта'), 'id': 'agreement'})

def privacy(request):

    return render(request, 'info/terms.html', {'info': Info.objects.get(title = 'Политика конфиденциальности'), 'id': 'privacy'})

def juridical(request):

    return render(request, 'info/juridical.html')

def online_payment_safety(request):

    return render(request, 'info/terms.html', {'info': Info.objects.get(title = 'Безопасность онлайн платежей'), 'id': 'payment-safety'})
    
def data_safety(request):

    return render(request, 'info/terms.html', {'info': Info.objects.get(title = 'Безопасность данных'), 'id': 'data-safety'})