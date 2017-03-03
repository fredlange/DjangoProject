from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    variables = {'content':['if you would like to contact','fredrik@uneedit.se']}
    return render(request, 'personal/contact.html', variables)

def sendmail(request):

    if request.POST:
        return redirect('/contact')

def aboutme(request):
    return render(request, 'personal/aboutme.html')
