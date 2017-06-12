from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse, HttpResponseRedirect
from models import Rocktaves, StandUp, StreetDance, PitchPerfect, RapWars
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from instamojo_wrapper import Instamojo
import re

api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN)


@csrf_exempt
def index(request):

	if request.method == 'POST':

		event_id = request.POST['form_id']


		########## Rocktaves ##########
		if int(event_id) == 0:

			email = request.POST['email']

			try:
				Rocktaves.objects.get(email_address = email)
				user_exists = True
			except:
				user_exists = False

			if user_exists:

				data = {'status':0}
				return JsonResponse(data)

			mobile_number = request.POST['phone']

			if len(mobile_number) == 10:
				try:

					number = int(mobile_number)

					rocktaves = Rocktaves()
					rocktaves.name = request.POST['name']
					rocktaves.city = request.POST['city']
						
					if request.POST['gender'] == 'M':
						rocktaves.gender = 'Male'
					elif request.POST['gender'] == 'F':
						rocktaves.gender = 'Female'

					rocktaves.phone = '+91' + mobile_number
					rocktaves.email_address = email
					rocktaves.save()
					name = request.POST['name']
					data = {'status':1,'email':email, 'name':name, 'Event':'Rocktaves'}
						
					return JsonResponse(data)

				except ValueError:
					data = {'status':2}
					return JsonResponse(data)

			else:
				data = {'status':2}
				return JsonResponse(data)


		########## PitchPerfect ##########

		if int(event_id) == 1:

			g_l = request.POST['group+lead']

			g_m = request.POST['group+memb']
			email = request.POST['email']

			try:
				PitchPerfect.objects.get(email_address = email)
				user_exists = True
			except:
				user_exists = False

			if user_exists:

				data = {'status':0}
				return JsonResponse(data)

			mobile_number = request.POST['phone']
			email = request.POST['email']

			if len(mobile_number) == 10:
				try:

					number = int(mobile_number)

					

					pitch_perfect = PitchPerfect()
					pitch_perfect.g_leader = g_l
					pitch_perfect.members = g_m
					pitch_perfect.city = request.POST['city']
					pitch_perfect.college = request.POST['college']
					pitch_perfect.phone = '+91' + mobile_number
					pitch_perfect.email_address = email
					pitch_perfect.save()
					name = g_l
					#data = {'status':1,'email':email, 'name':name, 'Event':'Pitch Perfect'}
					
					response = api.payment_request_create(buyer_name= g_l,
						email= email,
						phone= number,
						amount = 250,
						purpose="Pitch Perfect",
						redirect_url= request.build_absolute_url(reverse("API Request"))
						)
					
					return HttpResponseRedirect(response['payment_request']['longurl'])

				except ValueError:
					data = {'status':2}
					return JsonResponse(data)

			else:
				data = {'status':2}
				return JsonResponse(data)



		########## RapWars ##########


		if int(event_id) == 2:

			email = request.POST['email']

			try:
				RapWars.objects.get(email_address = email)
				user_exists = True
			except:
				user_exists = False

			if user_exists:

				data = {'status':0}
				print "Exists"
				return JsonResponse(data)

			mobile_number = request.POST['phone']

			if len(mobile_number) == 10:
				try:

					number = int(mobile_number)
					rapwars = RapWars()
					rapwars.name = request.POST['name']
					rapwars.city = request.POST['city']
						
					if request.POST['gender'] == 'M':
						rapwars.gender = 'Male'
					elif request.POST['gender'] == 'F':
						rapwars.gender = 'Female'

					rapwars.phone = '+91' + mobile_number
					rapwars.email_address = email
					rapwars.save()
					name = request.POST['name']
					data = {'status':1,'email':email, 'name':name, 'Event':'RapWars'}
						
					return JsonResponse(data)

				except ValueError:
					data = {'status':2}
					return JsonResponse(data)

			else:
				data = {'status':2}
				return JsonResponse(data)


		########## Street Dance ##########		


		if int(event_id) == 3:

			
			g_l = request.POST['group+lead']

			g_m = request.POST['group+memb']
			

			email = request.POST['email']

			try:
				StreetDance.objects.get(email_address = email)
				user_exists = True
			except:
				user_exists = False

			if user_exists:

				data = {'status':0}
				return JsonResponse(data)

			mobile_number = request.POST['phone']

			if len(mobile_number) == 10:
				try:

					number = int(mobile_number)
					
					street_dance = StreetDance()
					street_dance.g_leader = g_l
					street_dance.members = g_m
					street_dance.city = request.POST['city']
					street_dance.college = request.POST['college']
					street_dance.phone = '+91' + mobile_number
					street_dance.email_address = email
					street_dance.save()
					name = g_l
					data = {'status':1,'email':email, 'name':name, 'Event':'Street Dance'}
					
					response = api.payment_request_create(
						buyer_name= g_l,
						email = email,
						phone = number,
						amount = 250,
						purpose = "Street Dance",
						redirect_url = request.build_absolute_url(reverse("API Request"))
						)
					
					return HttpResponseRedirect(response['payment_request']['longurl'])

					

				except ValueError:
					data = {'status':2}
					return JsonResponse(data)

			else:
				data = {'status':2}
				return JsonResponse(data)



		########## Humor Fest ##########		


		if int(event_id) == 4:
		
			email = request.POST['email']

			try:
				StandUp.objects.get(email_address = email)
				user_exists = True
			except:
				user_exists = False

			if user_exists:

				data = {'status':0}
				return JsonResponse(data)

			mobile_number = request.POST['phone']

			if len(mobile_number) == 10:
				try:

					number = int(mobile_number)

					standup = StandUp()
					standup.name = request.POST['name']
					standup.city = request.POST['city']
						
					if request.POST['gender'] == 'M':
						standup.gender = 'Male'
					elif request.POST['gender'] == 'F':
						standup.gender = 'Female'

					standup.phone = '+91' + mobile_number
					standup.email_address = email
					standup.save()
					name = request.POST['name']
					data = {'status':1,'email':email, 'name':name, 'Event':'StandUp SoapBox'}
					

					name = request.POST['name']

					response = api.payment_request_create(
						buyer_name = name,
						email = email,
						phone = number,
						amount = 250,
						purpose = "StandUp SandBox",
						redirect_url = request.build_absolute_url(reverse("API Request"))
						)
					
					return HttpResponseRedirect(response['payment_request']['longurl'])

					
				except ValueError:
					data = {'status':2}
					return JsonResponse(data)

			else:
				data = {'status':2}
				return JsonResponse(data)


	return render(request, 'preregistrations/index.html')

def apirequest(request):

	import requests
	payid=str(request.GET['payment_id'])
	headers = {'X-Api-Key': API_KEY,
    	       'X-Auth-Token': AUTH_TOKEN}
	r = requests.get('https://www.instamojo.com/api/1.1/payments/',
                	 headers=headers)
	json_ob = r.json()
	payments = json_ob['payments'][0]
	purpose = payments['purpose']
	email = payments['buyer_email']

	if "Pitch" in purpose:

		pitch_perfect = PitchPerfect.objects.get(email_address=email)
		pitch_perfect.paid = True
		pitch_perfect.save()

	if "Street" in purpose:

		street_dance = StreetDance.objects.get(email_address=email)
		street_dance.paid = True
		street_dance.save()

	if "StandUp" in purpose:

		stand_up = StandUp.objects.get(email_address=email)
		stand_up.paid = True
		stand_up.save()

	return render(request, 'preregistrations/index.html', {'message':'Payment Successful'})