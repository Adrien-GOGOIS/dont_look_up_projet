import requests
from datetime import date


class Asteroid():
    asteroid_id = 0
    name = ''
    diameter = 0
    close_approach_date = ''
    miss_distance = ''
    latest_approach = {}

    def __init__(self, asteroid_id, name, diameter, close_approach_date, miss_distance, latest_approach):
        self.asteroid_id = asteroid_id
        self.name = name
        self.diameter = diameter
        self.close_approach_date = close_approach_date
        self.miss_distance = miss_distance
        self.latest_approach = latest_approach


def get_asteroids(start_date, end_date):
    url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=' \
          + str(start_date) \
          + '&end_date=' \
          + str(end_date) \
          + '&api_key=vQWT6RYdaTlM3uhavzlzima97RJeaKZgSMMkqf6D'
    response = requests.get(url)
    asteroids = response.json()

    asteroids_list = []

    for date, asteroid in asteroids['near_earth_objects'].items():
        asteroid_id = asteroid[0]['id']
        name = asteroid[0]['name']
        diameter = asteroid[0]['estimated_diameter']['meters']['estimated_diameter_max']
        close_approach_date = asteroid[0]['close_approach_data'][0]['close_approach_date']
        miss_distance = asteroid[0]['close_approach_data'][0]['miss_distance']['kilometers']
        latest_approach = {}

        asteroid = Asteroid(asteroid_id, name, diameter, close_approach_date, miss_distance, latest_approach)
        asteroids_list.append(asteroid)

    return asteroids_list


def get_asteroid_by_id(asteroid_id):
    url = 'https://api.nasa.gov/neo/rest/v1/neo/' \
          + str(asteroid_id) \
          + '?api_key=vQWT6RYdaTlM3uhavzlzima97RJeaKZgSMMkqf6D'
    response = requests.get(url)
    asteroid = response.json()

    asteroid_approach = asteroid['close_approach_data']

    asteroid_latest_approach = {}

    for approach in reversed(asteroid_approach):
        if approach['close_approach_date'] < str(date.today()):
            asteroid_latest_approach.update({approach['close_approach_date']: approach['miss_distance']['kilometers']})
        if len(asteroid_latest_approach) == 5:
            break

    asteroid_id = asteroid['id']
    name = asteroid['name']
    diameter = 0
    close_approach_date = ''
    miss_distance = ''

    asteroid = Asteroid(asteroid_id, name, diameter, close_approach_date, miss_distance, asteroid_latest_approach)

    return asteroid
