# ParkingLotDataCollection
ParkingLotDataCollection is written and tested in Python 3.6.2. Its purpose is to unify parking lot data from APIs in Germany.

## How does it work:

The main file "ParkingLotDataCollection.py" includes the data aggregators from each city and combines and saves the data into one file (under the [savedData]() subfolder).

Staged data / raw data will be loaded to the [loading]() subfolder and overwritten.

## Sources:
https://www.govdata.de/apps/-/details/parkhaeuser-bn; License: Limited usage

https://offenedaten-koeln.de/dataset/parkhausbelegung; License: Creative Commons Namensnennung 3.0 DE

http://offenedaten.frankfurt.de/dataset/parkdaten-dynamisch; License: Datenlizenz Deutschland Namensnennung

https://offenedaten.de/dataset/parkhauser-munchen; License: dl-de-by-2.0 None 

## Limitations:

1. Bremen: No real time access for data: https://offenedaten.de/api/3/action/package_show?id=parkhauser-in-bremen1, e.g. https://kunden.login.bremen.de/sixcms/detail.php?template=export_poi_d&kat=parken

2. Braunschweig: No real time access for data: https://offenedaten.de/api/3/action/package_show?id=parkangebote-und-aktuelle-parksituation-in-der-innenstadt-braunschweig

3. Münster: No real time access for data: https://offenedaten.de/dataset/parkleitsystem-api-munster, e.g. http://parkleit-api.codeformuenster.org/ returns 404 error

4. Hamburg: Only snapshot access for data: https://offenedaten.de/api/3/action/package_show?id=parkraumgis-hamburg2, e.g.
http://archiv.transparenz.hamburg.de/hmbtgarchive/HMDK/hh_wfs_parkraum_12663_snap_1.XML no data on parking lot usage

5. Cologne: No parking lot status information, only overview: http://www.stadt-koeln.de/externe-dienste/open-data/parking-ts.php

6. Düsseldorf: Not sure if the data can be trusted. Does not seem to be very official: http://datarun.s3.amazonaws.com/parkdaten_Duesseldorf.geojson

7. Kassel: Not sure if the data can be trusted. Does not seem to be very official: http://datarun.s3.amazonaws.com/parkdaten_Kassel.geojson


## Further links:

### Allgemein:
https://www.mcloud.de/web/guest/suche/-/results/searchAction?_mysearchportlet_query=parkplatzbelegung
https://offenedaten.de/dataset?q=parkh%C3%A4user&sort=score+desc%2C+metadata_modified+desc

### Bonn:
https://www.govdata.de/apps/-/details/parkhaeuser-bn
https://opendata.bonn.de/dataset/parkh%C3%A4user-parkhausbelegung
https://www.europeandataportal.eu/data/de/dataset/parkhaeuser-bn

### Frankfurt:
http://offenedaten.frankfurt.de/dataset/parkdaten-dynamisch
https://www.mcloud.de/web/guest/suche/-/results/detail/mdmparkdatenfrankfurt?_mysearchportlet_backURL=https%3A%2F%2Fwww.mcloud.de%2Fweb%2Fguest%2Fsuche%2F-%2Fresults%2FsearchAction%3F_mysearchportlet_query%3Dparkplatzbelegung%26_mysearchportlet_page%3D1&_mysearchportlet_query=parkplatzbelegung
http://datarun.s3.amazonaws.com/parkdaten_Frankfurt.geojson

### Köln:
https://offenedaten-koeln.de/dataset/parkhausbelegung

### Hamburg:
https://www.govdata.de/daten/-/details/parkhauser-hamburg7

### Braunschweig:
https://offenedaten.de/dataset/parkangebote-und-aktuelle-parksituation-in-der-innenstadt-braunschweig

### Münster:
https://offenedaten.de/dataset/parkleitsystem-api-munster

### München:
https://offenedaten.de/dataset/parkhauser-munchen

### Düsseldorf:
https://www.mcloud.de/web/guest/suche/-/results/detail/mdmparkdatenstadtdsseldorf?_mysearchportlet_backURL=https%3A%2F%2Fwww.mcloud.de%2Fweb%2Fguest%2Fsuche%2F-%2Fresults%2FsearchAction%3F_mysearchportlet_query%3Dparkplatzbelegung%26_mysearchportlet_page%3D1&_mysearchportlet_query=parkplatzbelegung
http://datarun.s3.amazonaws.com/parkdaten_Duesseldorf.geojson

### Kassel:
https://www.mcloud.de/web/guest/suche/-/results/detail/mdmparkdatenkassel?_mysearchportlet_backURL=https%3A%2F%2Fwww.mcloud.de%2Fweb%2Fguest%2Fsuche%2F-%2Fresults%2FsearchAction%3F_mysearchportlet_query%3Dparkplatzbelegung%26_mysearchportlet_page%3D1&_mysearchportlet_query=parkplatzbelegung
http://datarun.s3.amazonaws.com/parkdaten_Kassel.geojson