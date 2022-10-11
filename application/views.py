from django.shortcuts import render
from application.form import DateForm
from application.service import get_asteroids
from application.service import get_asteroid_by_id
from django.contrib import messages


def homepage(request):
    asteroids = []

    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            asteroids = get_asteroids(start_date, end_date)

            if not asteroids:
                messages.error(request, "L'intervalle entre 2 dates ne doit pas être supérieur à 7 jours")

    else:
        form = DateForm()

    context = {
        'form': form,
        'asteroids': asteroids,
    }

    return render(request, 'application/homepage.html', context)


def asteroid_details(request, asteroid_id):
    asteroid = get_asteroid_by_id(asteroid_id)

    context = {
        'asteroid': asteroid,
    }

    return render(request, 'application/asteroid_details.html', context)
