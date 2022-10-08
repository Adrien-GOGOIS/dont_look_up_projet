import requests


def get_asteroids(start_date, end_date):
    url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=' + start_date + '&end_date=' + end_date + '&api_key=DEMO_KEY'
    r = requests.get(url)
    print(r.json())


get_asteroids('2022-10-05', '2022-10-08')