from django.http import HttpResponse
# Create your views here.


def blog(request):
    print('blog')
    return HttpResponse('blog do app')
