import requests
import sys
import xml.etree.ElementTree as ET
import Bonn
import Frankfurt
import Cologne
import datetime

def loadAllData():
	"Loads all parking data"
	id, bonnData = Bonn.loadData(0)
	id, frankfurtData = Frankfurt.loadData(id)
	id, cologneData = Cologne.loadData(id)
	data = bonnData + frankfurtData + cologneData
	dateTime = datetime.datetime.now().isoformat().replace(":", "-").replace(".", "-")
	with open('./savedData/' + dateTime + '.json', 'w') as f:
		f.write('[' + ','.join(data) + ']')
	print ("Done")

loadAllData()