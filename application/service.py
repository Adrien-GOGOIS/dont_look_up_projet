import requests


def get_asteroids(start_date, end_date):
    url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=' \
          + start_date \
          + '&end_date=' \
          + end_date \
          + '&api_key=vQWT6RYdaTlM3uhavzlzima97RJeaKZgSMMkqf6D'
    response = requests.get(url)
    asteroids = response.json()

    for date, asteroid in asteroids['near_earth_objects'].items():
        print("Date : " + date)
        print("ID : " + asteroid[0]['id'])
        print("Name : " + asteroid[0]['name'])


get_asteroids('2022-10-05', '2022-10-08')
