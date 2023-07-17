import datetime
import requests
from datetime import date
from api_key import get_key
from application.models.models import ImageOfTheDay
import translators as ts

class ImageService:
	api_key = get_key()

	def get_image_of_the_day(self, date: datetime) -> ImageOfTheDay:
		url = 'https://api.nasa.gov/planetary/apod?' \
			+ 'date=' \
			+ str(date) \
			+ '&api_key=' \
			+ self.api_key
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


	def get_translation(self, text):
		return ts.translate_text(text, translator='google', from_language='en', to_language='fr')