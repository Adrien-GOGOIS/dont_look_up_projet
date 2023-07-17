from django.shortcuts import render
from application.services.AsteroidService import AsteroidService


def asteroid_details(request, asteroid_id):
	asteroidServiceInstance = AsteroidService()
	asteroid = asteroidServiceInstance.get_asteroid_by_id(asteroid_id)

	context = {
        'asteroid': asteroid,
    }
	return render(request, 'application/asteroidDetails/asteroid_details.html', context)