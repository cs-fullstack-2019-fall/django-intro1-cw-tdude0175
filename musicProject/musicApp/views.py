from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is a bad request. Start with the music route.")

def music(request):
    return HttpResponse("welcome to the music route. try artist1, artist2, artist3")

def artist1(request):
    return HttpResponse("Daft Punk is a two man techno band from france.")

def artist2(request):
    return HttpResponse("Metallica gained the nickname 'alchollica' on tours with other bands due to the amount of drinks they would often have.")

def artist3(request):
    return HttpResponse("Guns and roses lead singer Axel is not a nice person.")