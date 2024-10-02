from django.http import HttpResponse

# Create your views here.


def home(request):
    print('home')
    return HttpResponse('home que veio do app')
