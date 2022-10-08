from django.shortcuts import render

# Create your views here.
def homepage(request):
    context = {
    }

    return render(request, 'application/homepage.html', context)


def asteroids_list(request):
    context = {
    }

    return render(request, 'application/asteroids_list.html', context)


def asteroid_details(request, asteroid_id):
    context = {
        'asteroid_id': asteroid_id,
    }

    return render(request, 'application/asteroid_details.html', context)