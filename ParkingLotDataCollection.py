import sys
import datetime
import Bonn
import Cologne
import Frankfurt
import Munich

def loadAllData():
	"Loads all parking data"
	id, bonnData = Bonn.loadData(0)
	id, frankfurtData = Frankfurt.loadData(id)
	id, cologneData = Cologne.loadData(id)
	id, munichData = Munich.loadData(id)
	data = bonnData + frankfurtData + cologneData + munichData
	dateTime = getCurrentDateTimeFormatted()
	with open('./savedData/' + dateTime + '.json', 'w') as f:
		f.write('[' + ','.join(data) + ']')
	print ("Done")
	
def getCurrentDateTimeFormatted():
	"Returns a string for the json output file with the current date and time"
	return datetime.datetime.now().isoformat().replace(":", "-").replace(".", "-")

loadAllData()