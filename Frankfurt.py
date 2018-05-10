import requests
import sys
import xml.etree.ElementTree as ET

baseUrl = '{http://datex2.eu/schema/2/2_0}'
filePath = './loading/frankfurt.xml'

def loadData(id):
	"Loads parking lot data for the city Frankfurt"
	response = requests.get("http://offenedaten.frankfurt.de/dataset/912fe0ab-8976-4837-b591-57dbf163d6e5/resource/48378186-5732-41f3-9823-9d1938f2695e/download/parkdatendyn.xml")
	with open(filePath, 'wb') as f:
		f.write(response.content)
	tree = ET.parse(filePath)
	root = tree.getroot()
	data = []
	id, parkingAreaData = loadParkingAreas(data, root, id)
	id, parkingFacilityData = loadParkingFacilities(data, root, id)
	return (id, parkingAreaData + parkingFacilityData)
	
def loadParkingAreas(data, root, id):
	"Loads all data for parking areas"
	for parkingArea in root.iter(baseUrl + 'parkingAreaStatus'):
		parkingAreaId = parkingArea.find(baseUrl + 'parkingAreaReference')
		parkingAreaName = parkingAreaId.attrib['id'].split("[")[1].replace(']', '')
		parkingAreaStatusTime = parkingArea.find(baseUrl + 'parkingAreaStatusTime').text
		parkingAreaTotalNumber = parkingArea.find(baseUrl + 'parkingAreaTotalNumberOfVacantParkingSpaces').text
		data.append('{"id":"' + str(id) + '", "name":"' + parkingAreaName + '", "latitude":"Unknown", "longitude":"Unknown", "totalParkingLots":"' + \
		parkingAreaTotalNumber + '", "freeParkingLots":"Unknown", "height":"Unknown", "trend":"Unknown", "status":"Unknown", "timestamp":"' + \
		parkingAreaStatusTime + '", "prices":"Unknown", "type":"Car park area", "numberOfDisabledParkingLots":"Unknown", ' + \
		'"freeDisabledParkingLots":"Unknown", "numberOfElectroParkingLots":"Unknown", "freeOfElectroParkingLots":"Unknown", "numberOfFamilyParkingLots":"Unknown", ' + \
		'"freeOfFamilyParkingLots":"Unknown", "numberOfWomenParkingLots":"Unknown", "freeOfWomenParkingLots":"Unknown", "numberOfPremiumParkingLots":"Unknown", ' + \
		'"freeOfPremiumParkingLots":"Unknown", "premiumParkingLotPrices":"Unknown", "openingTimes":"Unknown", "address":{ "country":"Germany", ' + \
		'"state":"Hessen", "city":"Frankfurt", "zipCode":"Unknown", "street":"Unknown", "houseNumber":"Unknown", ' + \
		'"additionalInformation":"Unknown" }, "operator":"Unknown", "telephone":"Unknown", "website": "Unknown"}')
		id = id + 1
	return (id, data)
	
def loadParkingFacilities(data, root, id):
	"Loads all data for parking areas"
	for parkingFacility in root.iter(baseUrl + 'parkingFacilityStatus'):
		parkingFacilityId = parkingFacility.find(baseUrl + 'parkingFacilityReference')
		if(parkingFacilityId is None):
			continue
		parkingFacilityName = parkingFacilityId.attrib['id'].split("[")[1].replace(']', '')
		parkingFacilityStatusTime = parkingFacility.find(baseUrl + 'parkingFacilityStatusTime').text
		parkingFacilityTotalNumber = parkingFacility.find(baseUrl + 'totalParkingCapacityOverride').text	
		parkingFacilityStatus = parkingFacility.find(baseUrl + 'parkingFacilityStatus').text.title()
		parkingFacilityFreeParkingLots = parkingFacility.find(baseUrl + 'totalNumberOfVacantParkingSpaces')
		if(parkingFacilityFreeParkingLots is None):
			parkingFacilityFreeParkingLots = 'Unknown'
		else:
			parkingFacilityFreeParkingLots = parkingFacilityFreeParkingLots.text
		data.append('{"id":"' + str(id) + '", "name":"' + parkingFacilityName + '", "latitude":"Unknown", "longitude":"Unknown", "totalParkingLots":"' + \
		parkingFacilityTotalNumber + '", "freeParkingLots":"' + parkingFacilityFreeParkingLots + '", "height":"Unknown", "trend":"Unknown", "status":"' + \
		parkingFacilityStatus + '", "timestamp":"' + parkingFacilityStatusTime + '", "prices":"Unknown", "type":"Car park", "numberOfDisabledParkingLots":"Unknown", ' + \
		'"freeDisabledParkingLots":"Unknown", "numberOfElectroParkingLots":"Unknown", "freeOfElectroParkingLots":"Unknown", "numberOfFamilyParkingLots":"Unknown", ' + \
		'"freeOfFamilyParkingLots":"Unknown", "numberOfWomenParkingLots":"Unknown", "freeOfWomenParkingLots":"Unknown", "numberOfPremiumParkingLots":"Unknown", ' + \
		'"freeOfPremiumParkingLots":"Unknown", "premiumParkingLotPrices":"Unknown", "openingTimes":"Unknown", "address":{ "country":"Germany", ' + \
		'"state":"Hessen", "city":"Frankfurt", "zipCode":"Unknown", "street":"Unknown", "houseNumber":"Unknown", ' + \
		'"additionalInformation":"Unknown" }, "operator":"Unknown", "telephone":"Unknown", "website": "Unknown"}')
		id = id + 1
	return (id, data)