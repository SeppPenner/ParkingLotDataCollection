import requests
import sys
import json
import datetime

filePath = './loading/munich.json'

def loadData(id):
	"Loads parking lot data for the city Munich"
	dateStamp = f"{datetime.datetime.now():%Y-%m-%d}"
	url = 'https://www.opengov-muenchen.de/dataset/addaa7d4-40be-4621-846e-c5358cbe3f26/resource/76554a21-34bc-4f62-b609-8af20e0ad9d7/download/' + dateStamp +'parkhaeuser-muenchen.json'
	response = requests.get(url)
	with open(filePath, 'wb') as f:
		f.write(response.content)
	with open(filePath, 'r') as f:
		jsonData = json.load(f)
		data = []
		for place in jsonData['places']:
			name = place['title']
			street = place['street']
			houseNumber = place['streetNumber']
			location = place['location']
			latitude = location['lat']
			longitude = location['lng']
			link = place['urlInPortal']
			data.append('{"id":"' + str(id) + '", "name":"' + name.title() + '",' + \
			'"latitude":"' + str(latitude) + '", "longitude":"' + str(longitude) + '", "totalParkingLots":"Unknown", "freeParkingLots":"Unknown", "height":"Unknown", ' + \
			'"trend":"Unknown", "status":"Unknown", "timestamp":"Unknown", "prices":"Unknown",' + '"type":"Unknown", "numberOfDisabledParkingLots":"Unknown", ' + \
			'"freeDisabledParkingLots":"Unknown", "numberOfElectroParkingLots":"Unknown", "freeOfElectroParkingLots":"Unknown", "numberOfFamilyParkingLots":"Unknown", ' + \
			'"freeOfFamilyParkingLots":"Unknown", "numberOfWomenParkingLots":"Unknown", "freeOfWomenParkingLots":"Unknown", "numberOfPremiumParkingLots":"Unknown", ' + \
			'"freeOfPremiumParkingLots":"Unknown", "premiumParkingLotPrices":"Unknown", "openingTimes":"Unknown", "address":{ "country":"Germany", ' + \
			'"state":"Bavaria", "city":"Munich", "zipCode":"Unknown", "street":"' + street + '", "houseNumber":"' + str(houseNumber) + '", ' + \
			'"additionalInformation":"Unknown" }, "operator":"Unknown", "telephone":"Unknown", "website": "' + link + '"}')
			id = id + 1
	return (id, data)
	
loadData(10)