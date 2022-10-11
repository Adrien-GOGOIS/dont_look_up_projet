from django.shortcuts import render
from application.form import DateForm
from application.service import get_asteroids
from application.service import get_asteroid_by_id


def homepage(request):
    asteroids = []

    if request.method == 'POST':
        form = DateForm(request.POST)
        is_loading = True
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


def asteroid_details(request, asteroid_id):
    asteroid = get_asteroid_by_id(asteroid_id)

    context = {
        'asteroid': asteroid,
    }

    return render(request, 'application/asteroid_details.html', context)
