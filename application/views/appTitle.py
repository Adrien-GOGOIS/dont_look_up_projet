from django.shortcuts import render


def app_title(request):
    return render(request, 'application/app_title.html')
