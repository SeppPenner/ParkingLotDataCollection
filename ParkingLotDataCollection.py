import requests
import sys
import xml.etree.ElementTree as ET
import Bonn
import datetime

def loadAllData():
	"Loads all parking data"
	id = 0		
	bonnData = Bonn.loadBonnData(id)
	dateTime = datetime.datetime.now().isoformat()
	with open('./savedData/' + dateTime + '.json', 'w') as f:
		f.write(bonnData)
	print ("Done")

loadAllData()