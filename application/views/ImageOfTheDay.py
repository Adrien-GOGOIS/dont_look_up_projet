from django.shortcuts import render
from application.forms.form import ImageForm
from application.services.ImageService import ImageService
from django.contrib import messages


def image_of_the_day(request):
	imageServiceInstance = ImageService()
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
				image = imageServiceInstance.get_image_of_the_day(date)
				if image:
					translation = imageServiceInstance.get_translation(image.explanation)
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