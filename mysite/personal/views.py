from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import personal.forms as Form

# Email imports
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

# Create your views here.

def index(request):
    return render(request, 'personal/home.html')


def contact(request):

    form_class = Form.ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            message = request.POST.get('content', '')

            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email':contact_email,
                'content': message
            })

            content = template.render(context)
            #content = str(contact_name + "<br>" + contact_email + "<br>" + form_content)

            email = EmailMessage(
                'New contact from website', # Rubrik
                content, # Innehåll
                'from@mail.com', # Avsändare
                ['to@mail.com'], # Mottagare (lista)
                headers = {'reply-to': contact_email}
            )

            email.send()
            return redirect('contact')


    variables = {
        'content':['if you would like to contact','fredrik@uneedit.se'],
        'form': Form.ContactForm
    }
    return render(request, 'personal/contact.html', variables)

def aboutme(request):
    return render(request, 'personal/aboutme.html')
