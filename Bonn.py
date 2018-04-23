import requests
import sys
import xml.etree.ElementTree as ET

def loadBonnData(id):
	"Loads parking lot data for the city Bonn"
	response = requests.get("http://www.bcp-bonn.de/stellplatz/bcpinfo.xml") #1= gleichbleibend, 3=“Freie Plätze“ fallend, 2 = “Freie Plätze“ steigend, Status 0 = geöffnet, 1= geschlossen 
	with open('./loading/bonn.xml', 'wb') as f:
		f.write(response.content)
	tree = ET.parse('./loading/bonn.xml')
	root = tree.getroot()
	data = []
	for parkingSpace in root.findall('parkhaus'):
		number = parkingSpace.find('lfdnr').text
		status = parkingSpace.find('status').text
		data.append('{"id":"' + getIdForBonn(number) + '", "name":"' + parkingSpace.find('bezeichnung').text.replace(".txt", "").title() + '",' + \
		'"latitude":"' + getLatitudeForBonn(id) + '", "longitude":"' + getLongitudeForBonn(id) + '", "totalParkingLots":"' + \
		parkingSpace.find('gesamt').text + '", "freeParkingLots":"' + parkingSpace.find('frei').text + '", "trend":"' + parkingSpace.find('tendenz').text + \
		'", "status":"' + getStatusForBonn(status) + '", "timestamp":"' + parkingSpace.find('zeitstempel').text + '", "prices":"1 € per hour",' + \
		'"type":"Car park", "numberOfDisabledParkingLots":"Unknown", "freeDisabledParkingLots":"Unknown", "numberOfElectroParkingLots":"Unknown",' + \
		'"freeOfElectroParkingLots":"Unknown", "numberOfFamilyParkingLots":"Unknown", "freeOfFamilyParkingLots":"Unknown", "numberOfWomenParkingLots":"Unknown",' + \
		'"freeOfWomenParkingLots":"Unknown", "numberOfPremiumParkingLots":"Unknown", "freeOfPremiumParkingLots":"Unknown",' + \
		'"premiumParkingLotPrices":"Unknown", "openingTimes":"Unknown", "address":{ "country":"Unknown", "state":"Unknown",' + \
		'"city":"Unknown", "zipCode":"Unknown", "street":"Unknown", "houseNumber":"Unknown", "additionalInformation":"Unknown" }, "operator":"Unknown"}')
		id = id + 1
	return '[' + ','.join(data) + ']'

def getLatitudeForBonn(id):
	"Loads the latitude for a parking spot in Bonn by its number"
	if id == 0:
		return '50.7339257' #http://bcp-bonn.de/bahnhofgarage/
	if id == 1:
		return '50.7394424' #http://bcp-bonn.de/beethovenparkhaus/
	if id == 2:
		return '50.7369235' #http://bcp-bonn.de/friedensplatzgarage/
	if id == 3:
		return '50.7344313' #http://bcp-bonn.de/marktgarage/
	if id == 4:
		return '50.7357418' #http://bcp-bonn.de/muensterplatzgarage/
	if id == 5:
		return '50.7378037' #http://bcp-bonn.de/stadthausgarage/
	return 'Unknown'
	
def getLongitudeForBonn(id):
	"Loads the longitude for a parking spot in Bonn by its number"
	if id == 0:
		return '7.0936335' #http://bcp-bonn.de/bahnhofgarage/
	if id == 1:
		return '7.1010949' #http://bcp-bonn.de/beethovenparkhaus/
	if id == 2:
		return '7.0946575' #http://bcp-bonn.de/friedensplatzgarage/
	if id == 3:
		return '7.101642' #http://bcp-bonn.de/marktgarage/
	if id == 4:
		return '7.0921255' #http://bcp-bonn.de/muensterplatzgarage/
	if id == 5:
		return '7.0591477' #http://bcp-bonn.de/stadthausgarage/
	return 'Unknown'

def getIdForBonn(lfdnr):
	"Loads the id for a parking spot in Bonn by its internal lfdnr number"
	if lfdnr == '1':
		return '0'
	if lfdnr == '2':
		return '1'
	if lfdnr == '3':
		return '2'
	if lfdnr == '4':
		return '3'
	if lfdnr == '5':
		return '4'
	if lfdnr == '6':
		return '5'
	return '-1'

def getStatusForBonn(statusId):
	"Loads the id for a parking spot in Bonn by its internal lfdnr number"
	if statusId == '0':
		return 'Open'
	if statusId == '1':
		return 'Closed'
	return 'Unknown'