from django.shortcuts import render


# Create your views here.
def marquee(request):
    return render(request,'marquee.html')
