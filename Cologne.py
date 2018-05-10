import requests
import sys
import json

filePath = './loading/cologne.json'

def loadData(id):
	"Loads parking lot data for the city Cologne"
	response = requests.get("http://www.stadt-koeln.de/externe-dienste/open-data/parking-ts.php")
	with open(filePath, 'wb') as f:
		f.write(response.content)
	with open(filePath, 'r') as f:
		jsonData = json.load(f)
		data = []
		for feature in jsonData['features']:
			attributes = feature['attributes']
			coordinates = feature['geometry']
			name = attributes['PARKHAUS']
			if name is None:
				continue
			latitude = coordinates['y']
			longitude = coordinates['x']
			totalParkingLots = attributes['KAPAZITAET']
			timestamp = attributes['TIMESTAMP']
			trendId = str(attributes['TENDENZ'])
			data.append('{"id":"' + str(id) + '", "name":"' + name.title() + '", "latitude":"' + str(latitude) + '", "longitude":"' + str(longitude) + '", "totalParkingLots":"' + \
			str(totalParkingLots) + '", "freeParkingLots":"Unknown", "height":"Unknown", "trend":"' + getTrendFromNumber(trendId) + '", "status":"Unknown", "timestamp":"' + \
			timestamp + '", "prices":"Unknown", "type":"Unknown", "numberOfDisabledParkingLots":"Unknown", "freeDisabledParkingLots":"Unknown", ' + \
			'"numberOfElectroParkingLots":"Unknown", "freeOfElectroParkingLots":"Unknown", "numberOfFamilyParkingLots":"Unknown", ' + \
			'"freeOfFamilyParkingLots":"Unknown", "numberOfWomenParkingLots":"Unknown", "freeOfWomenParkingLots":"Unknown", "numberOfPremiumParkingLots":"Unknown", ' + \
			'"freeOfPremiumParkingLots":"Unknown", "premiumParkingLotPrices":"Unknown", "openingTimes":"", "address":{ "country":"Germany", ' + \
			'"state":"North Rhine-Westphalia", "city":"Cologne", "zipCode":"Unknown", "street":"Unknown", "houseNumber":"Unknown", ' + \
			'"additionalInformation":"Unknown" }, "operator":"Unknown", "telephone":"Unknown", "website": "Unknown"}')
			id = id + 1
	return (id, data)	

def getTrendFromNumber(number):
	"Gets the trend for a parkinglot in Cologne by the trend number"
	if number == '-1': #Tendenz: -1=nicht verfügbar
		return 'Not available' 
	if number == '0': #Tendenz: 0=gleichbleibend
		return 'Parking lots are staying constanly visited'
	if number == '1': #Tendenz: 1=weniger freie Plätze
		return 'Less free parking lots are available'
	if number == '2': #Tendenz: 2=mehr freie Plätze
		return 'More free parking lots are available'
	return 'Unknown'