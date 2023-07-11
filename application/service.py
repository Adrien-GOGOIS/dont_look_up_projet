import datetime
import requests
from datetime import date
from api_key import get_key
from application.models import Asteroid, LatestApproach, ImageOfTheDay

api_key = get_key()


def get_asteroids(start_date, end_date):

    asteroids_list = []

    if end_date - start_date > datetime.timedelta(days=7):
        return None

    url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=' \
          + str(start_date) \
          + '&end_date=' \
          + str(end_date) \
          + '&api_key=' \
          + api_key
    response = requests.get(url)
    asteroids = response.json()

    for date, asteroid in asteroids['near_earth_objects'].items():

        asteroid_id = asteroid[0]['id']
        name = asteroid[0]['name']
        diameter = round(asteroid[0]['estimated_diameter']['meters']['estimated_diameter_max'])
        close_approach_date = asteroid[0]['close_approach_data'][0]['close_approach_date']
        miss_distance = round(float(asteroid[0]['close_approach_data'][0]['miss_distance']['kilometers']))

        asteroid = Asteroid(
            asteroid_id=asteroid_id,
            name=name,
            diameter=diameter,
            close_approach_date=close_approach_date,
            miss_distance=miss_distance
        )
        asteroids_list.append(asteroid)

    return asteroids_list


def get_asteroid_by_id(asteroid_id):
    url = 'https://api.nasa.gov/neo/rest/v1/neo/' \
          + str(asteroid_id) \
          + '?api_key=' \
          + api_key
    response = requests.get(url)
    asteroid = response.json()

    actual_asteroid = Asteroid(asteroid_id=asteroid['id'], name=asteroid['name'])
    asteroid_approach = asteroid['close_approach_data']

    approaches_array = []
    count = 0

    for approach in reversed(asteroid_approach):
        if count < 5:
            if approach['close_approach_date'] < str(date.today()):
                asteroid_latest_approach = LatestApproach(
                    date=approach['close_approach_date'],
                    distance=round(float(approach['miss_distance']['kilometers'])),
                    asteroid=actual_asteroid
                )
                approaches_array.append(asteroid_latest_approach)
                count += 1

    return approaches_array


def get_image_of_the_day(date):
    url = 'https://api.nasa.gov/planetary/apod?' \
        + 'date=' \
        + str(date) \
        + '&api_key=' \
        + api_key
    response = requests.get(url)
    image_of_the_day = response.json()

    image = ImageOfTheDay(
        date=image_of_the_day['date'],
        explanation=image_of_the_day['explanation'],
        hdurl=image_of_the_day['hdurl'],
        title=image_of_the_day['title'],
        url=image_of_the_day['url'],
    )

    return image
