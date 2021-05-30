from django.http import HttpResponse

def contacts(request):
    return HttpResponse("This is the contacts page.")
