from django.shortcuts import render
from application.form import DateForm
from application.service import get_asteroids


def homepage(request):
    asteroids = []

    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            asteroids = get_asteroids(start_date, end_date)
    else:
        form = DateForm()

    context = {
        'form': form,
        'asteroids': asteroids
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
