from django.shortcuts import render
from application.forms.form import DateForm
from application.services.AsteroidService import AsteroidService
from django.contrib import messages


def homepage(request):
	asteroidServiceInstance = AsteroidService()
	asteroids = []
	
	if request.method == 'POST':
		form = DateForm(request.POST)
		if form.is_valid():
			start_date = form.cleaned_data['start_date']
			end_date = form.cleaned_data['end_date']

			asteroids = asteroidServiceInstance.get_asteroids(start_date, end_date)

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
