from django.shortcuts import render
from django.http import JsonResponse
import requests



def text_search(request):
	api_key ="AIzaSyCxa8xkGQ6b48BK9UwnmDoKylBWnF3EuPQ"
	query= request.GET.get("q",'')
	next_page_token = request.GET.get("next_page_token")
	url ='https://maps.googleapis.com/maps/api/place/textsearch/json?query=%s&key=%s'%(query,api_key)
	if next_page_token is not None:
		url+="&pagetoken=%s"%(next_page_token)

	response = requests.get(url)


	# return JsonResponse(response.json(),safe=False)

	return render(request,'text.html', {'response': response.json() })

def place_detail(request):
	api_key ="AIzaSyCxa8xkGQ6b48BK9UwnmDoKylBWnF3EuPQ"
	key ='AIzaSyAhm6E4TSv-TvQJRqW7qX7LeGPw1EaeA68'
	query= request.GET.get("r",'')
	
	url ='https://maps.googleapis.com/maps/api/place/details/json?reference=%s&key=%s'%(query,api_key)
	
	
	response = requests.get(url)



	# photo = 'https://maps.googleapis.com/maps/api/place/photo?photoreference=%s&key=%s&maxwidth=400'(photoreference,api_key)
	# photoreference= response.json(),results.reference
	# responsephoto = request.get(photo)

	
	# return JsonResponse(response.json(),safe=False)
	return render(request,'detail.html', {'response': response.json() , 'key':key , 'photo':responsephoto})



def nearby_search(request):
	api_key ="AIzaSyCxa8xkGQ6b48BK9UwnmDoKylBWnF3EuPQ"
	rad = request.GET.get("rad")
	lat = request.GET.get("lati")
	lon= request.GET.get("longitude")
	url ='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s,%s&radius=%s&key=%s'%(lat,lon,rad,api_key)
	response = requests.get(url)


	return render(request,'nearby.html', {'response': response.json()})
