from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.urls import reverse
from django.core.mail import EmailMessage

from .forms import ContactForm

def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # ENVIAMOS EL CORREO Y REDIRECCIONAMOS SI VA BIEN
            email = EmailMessage(
                'La Caffettiera: Nuevo mensaje de contacto',
                'De {} <{}> Escribio: {}'.format(name, email, content),
                'no-contestar@inbox.mailtrap.io',
                ['yama.hern@yahoo.com'],
                reply_to=[email]
            )

            try:
                email.send()
                #TODO SALIO BIEN
                return redirect(reverse('contact')+'?ok')
            except:
                # ALGO SALIO MAL
                return redirect(reverse('contact')+'?fail')

    return render(request, 'contact/contact.html', {'form':contact_form})