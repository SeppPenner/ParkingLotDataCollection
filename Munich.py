import requests
import sys
import xml.etree.ElementTree as ET

def loadData(id):
	"Loads parking lot data for the city Bonn"
	response = requests.get("http://www.bcp-bonn.de/stellplatz/bcpinfo.xml")
	with open('./loading/bonn.xml', 'wb') as f:
		f.write(response.content)
	tree = ET.parse('./loading/bonn.xml')
	root = tree.getroot()
	data = []
	for parkingSpace in root.findall('parkhaus'):
		number = parkingSpace.find('lfdnr').text
		status = parkingSpace.find('status').text
		trendId = parkingSpace.find('tendenz').text
		data.append('{"id":"' + getIdForBonn(number) + '", "name":"' + parkingSpace.find('bezeichnung').text.replace(".txt", "").title() + '",' + \
		'"latitude":"' + getLatitudeForBonn(id) + '", "longitude":"' + getLongitudeForBonn(id) + '", "totalParkingLots":"' + \
		parkingSpace.find('gesamt').text + '", "freeParkingLots":"' + parkingSpace.find('frei').text + '", "height":"' + getHeightForBonn(id) + \
		'", "trend":"' + getTrendForBonn(trendId) + '", "status":"' + getStatusForBonn(status) + '", "timestamp":"' + \
		parkingSpace.find('zeitstempel').text + '", "prices":"' + getPricesForBonn(id) + '",' + '"type":"Car park", "numberOfDisabledParkingLots":"Unknown", ' + \
		'"freeDisabledParkingLots":"Unknown", "numberOfElectroParkingLots":"Unknown", "freeOfElectroParkingLots":"Unknown", "numberOfFamilyParkingLots":"Unknown", ' + \
		'"freeOfFamilyParkingLots":"Unknown", "numberOfWomenParkingLots":"Unknown", "freeOfWomenParkingLots":"Unknown", "numberOfPremiumParkingLots":"Unknown", ' + \
		'"freeOfPremiumParkingLots":"Unknown", "premiumParkingLotPrices":"Unknown", "openingTimes":"' + getOpeningTimesForBonn(id) +'", "address":{ "country":"Germany", ' + \
		'"state":"North Rhine-Westphalia", "city":"Bonn", "zipCode":"53111", "street":"' + getStreetsForBonn(id) + '", "houseNumber":"Unknown", ' + \
		'"additionalInformation":"Unknown" }, "operator":"Bonner City Parkraum GmbH", "telephone":"02 28 / 96 99 191", "website": "' + getWebsiteForId(id) + '"}')
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
	
def getHeightForBonn(id):
	"Loads the height for a parking spot in Bonn by its number"
	if id == 0:
		return '2,00 m' #http://bcp-bonn.de/bahnhofgarage/
	if id == 1:
		return '1,90 m' #http://bcp-bonn.de/beethovenparkhaus/
	if id == 2:
		return '1,80 m' #http://bcp-bonn.de/friedensplatzgarage/
	if id == 3:
		return '1,80 m' #http://bcp-bonn.de/marktgarage/
	if id == 4:
		return '2,00 m' #http://bcp-bonn.de/muensterplatzgarage/
	if id == 5:
		return '2,10 m' #http://bcp-bonn.de/stadthausgarage/
	return 'Unknown'
	
def getPricesForBonn(id):
	"Loads the prices for a parking spot in Bonn by its number"
	if id == 0:
		return '1. and 2. hour: 1,30 €; 3. hour: 1,50 €; 4. and 5. hour: 2,00 €; from 6. hour: 2,50 €; night tarif: 1,00 € across-the-board;' + \
		'Tarif on sundays and holidays: 0,50 € per started hour; Maximum tarif: 25,00 € (on work days), 7,00 € (on sundays and holidays)'
		#http://bcp-bonn.de/bahnhofgarage/
	if id == 1:
		return '1. to 3. hour: 1,20 €; 4. hour: 1,50 €; 5. and 6. hour: 2,00 €; from the 7. hour: 2,50 €; Night tarif: 1,00 € across-the-board;' + \
		'Tarif on sundays and holidays: 0,50 € per started hour; Maximum tarif: 15,00 € (on work days), 7,00 € (on sundays and holidays); Extra price for some events: 3,00 €'
		#http://bcp-bonn.de/beethovenparkhaus/
	if id == 2:
		return '1. and 2. hour: 1,30 €; 3. hour: 1,50 €; 4. and 5. hour: 2,00 €; from 6. hour: 2,50 €; night tarif: 1,00 € across-the-board;' + \
		'Tarif on sundays and holidays: 0,50 € per started hour; Maximum tarif: 25,00 € (on work days), 7,00 € (on sundays and holidays)'
		#http://bcp-bonn.de/friedensplatzgarage/
	if id == 3:
		return '1. hour: 1,30 €; 2. hour: 1,40 €; 3. hour: 1,50 €; 4. and 5. hour: 2,00 €; from 6. hour: 2,50 €; night tarif: 1,00 € across-the-board;' + \
		'Tarif on sundays and holidays: 0,50 € per started hour; Maximum tarif: 25,00 € (on work days), 7,00 € (on sundays and holidays)'
		#http://bcp-bonn.de/marktgarage/
	if id == 4:
		return '1. hour: 1,30 €; 2. hour: 1,40 €; 3. hour: 1,50 €; 4. and 5. hour: 2,00 €; from 6. hour: 2,50 €; night tarif: 1,00 € across-the-board;' + \
		'Tarif on sundays and holidays: 0,50 € per started hour; Maximum tarif: 25,00 € (on work days), 7,00 € (on sundays and holidays)'
		#http://bcp-bonn.de/muensterplatzgarage/
	if id == 5:
		return '1. and 2. hour: 1,30 €; 3. hour: 1,50 €; 4. and 5. hour: 2,00 €; from 6. hour: 2,50 €; night tarif: 1,00 € across-the-board;' + \
		'Tarif on sundays and holidays: 0,50 € per started hour; Maximum tarif: 25,00 € (on work days), 7,00 € (on sundays and holidays)'
		#http://bcp-bonn.de/stadthausgarage/
	return 'Unknown'

def getOpeningTimesForBonn(id):
	"Loads the opening times for a parking spot in Bonn by its number"
	if id == 0:
		return 'Currently closed' #http://bcp-bonn.de/bahnhofgarage/
	if id == 1:
		return 'Monday to Thursday: 7:00 am to 1:00 am; Friday and Saturday: 7:00 am to 2:30 am; On sundays and holidays: 9:00 am to 1:00 am' #http://bcp-bonn.de/beethovenparkhaus/
	if id == 2:
		return 'Monday to Thursday: 7:00 am to 1:00 am; Friday and Saturday: 7:00 am to 2:30 am; On sundays and holidays: 9:00 am to 1:00 am' #http://bcp-bonn.de/friedensplatzgarage/
	if id == 3:
		return 'Open 24 hours a day' #http://bcp-bonn.de/marktgarage/
	if id == 4:
		return 'Monday to Thursday: 7:00 am to 1:00 am; Friday and Saturday: 7:00 am to 2:30 am; On sundays and holidays: 9:00 am to 1:00 am' #http://bcp-bonn.de/muensterplatzgarage/
	if id == 5:
		return 'Open 24 hours a day' #http://bcp-bonn.de/stadthausgarage/
	return 'Unknown'
	
def getStreetsForBonn(id):
	"Loads the street names for a parking spot in Bonn by its number"
	if id == 0:
		return 'Münsterstraße' #http://bcp-bonn.de/bahnhofgarage/
	if id == 1:
		return 'Engeltalstraße' #http://bcp-bonn.de/beethovenparkhaus/
	if id == 2:
		return 'Oxfordstraße' #http://bcp-bonn.de/friedensplatzgarage/
	if id == 3:
		return 'Stockenstraße' #http://bcp-bonn.de/marktgarage/
	if id == 4:
		return 'Budapester Straße' #http://bcp-bonn.de/muensterplatzgarage/
	if id == 5:
		return 'Weiherstraße' #http://bcp-bonn.de/stadthausgarage/
	return 'Unknown'
	
def getWebsiteForId(id):
	"Loads the website names for a parking spot in Bonn by its number"
	if id == 0:
		return 'http://bcp-bonn.de/bahnhofgarage/' #http://bcp-bonn.de/bahnhofgarage/
	if id == 1:
		return 'http://bcp-bonn.de/beethovenparkhaus/' #http://bcp-bonn.de/beethovenparkhaus/
	if id == 2:
		return 'http://bcp-bonn.de/friedensplatzgarage/' #http://bcp-bonn.de/friedensplatzgarage/
	if id == 3:
		return 'http://bcp-bonn.de/marktgarage/' #http://bcp-bonn.de/marktgarage/
	if id == 4:
		return 'http://bcp-bonn.de/muensterplatzgarage/' #http://bcp-bonn.de/muensterplatzgarage/
	if id == 5:
		return 'http://bcp-bonn.de/stadthausgarage/' #http://bcp-bonn.de/stadthausgarage/
	return 'Unknown'
	
def getTrendForBonn(trendId): #Tendenz: 1=gleichbleibend, 2="Freie Plätze" steigend, 3="Freie Plätze" fallend
	"Loads the id for a parking spot in Bonn by its internal lfdnr number"
	if trendId == '1':
		return 'Parking lots are staying constanly visited'
	if trendId == '2':
		return 'More free parking lots are available'
	if trendId == '3':
		return 'Less free parking lots are available'
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

def getStatusForBonn(statusId): #Status: 0=geöffnet, 1=geschlossen
	"Loads the id for a parking spot in Bonn by its internal lfdnr number"
	if statusId == '0':
		return 'Open'
	if statusId == '1':
		return 'Closed'
	return 'Unknown'