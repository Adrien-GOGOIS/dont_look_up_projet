from datetime import date
from django.shortcuts import render
from application.form import DateForm, ImageForm
from application.service import get_asteroids, get_image_of_the_day, get_translation
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
                messages.error(
                    request, "L'intervalle entre 2 dates ne doit pas être supérieur à 7 jours. \n "
                             "Le but de cette application n'étant pas de vous donner le temps de fuir."
                )

            if start_date > end_date:
                messages.error(request, "Sur Terre, la fin se déroule après le début...")
    else:
        form = DateForm()
    context = {
        'form': form,
        'asteroids': asteroids,
    }

    return render(request, 'application/homepage/homepage.html', context)


def asteroid_details(request, asteroid_id):
    asteroid = get_asteroid_by_id(asteroid_id)

    context = {
        'asteroid': asteroid,
    }

    return render(request, 'application/asteroidDetails/asteroid_details.html', context)


def image_of_the_day(request):
    image = []
    translation = ''
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']

            if date > date.today():
                messages.error(
                    request, "Ne pas choisir de date future"
                )
            else:
                image = get_image_of_the_day(date)
                if image:
                    translation = get_translation(image.explanation)
                else:
                    messages.error(
                        request, "Pas d'image"
                    )	
    else:
        form = ImageForm()

    context = {
        'form': form,
        'image': image,
        'translation': translation
    }

    return render(request, 'application/ImageOfTheDay/image_of_the_day.html', context)


def app_title(request):
    return render(request, 'application/app_title.html')
