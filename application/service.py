import requests


class Asteroid():
    asteroid_id = 0
    name = ''
    diameter = 0
    close_approach_date = ''
    miss_distance = ''

    def __init__(self, asteroid_id, name, diameter, close_approach_date, miss_distance):
        self.asteroid_id = asteroid_id
        self.name = name
        self.diameter = diameter
        self.close_approach_date = close_approach_date
        self.miss_distance = miss_distance


def get_asteroids(start_date, end_date):
    print('request...')
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

        asteroid = Asteroid(asteroid_id, name, diameter, close_approach_date, miss_distance)
        asteroids_list.append(asteroid)

    return asteroids_list
