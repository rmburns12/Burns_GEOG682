#GEOG682 Lab 4
#Rob Burns
#4/18/2020
districts = "S:/682/Spring20/rburns12/Labs/Lab4/Data/Districts/Police_Districts.shp" 
iface.addVectorLayer(districts,"districts","ogr") 
crime = "S:/682/Spring20/rburns12/Labs/Lab4/Data/Crime/Crime_Incidents_in_2017.shp" 
iface.addVectorLayer(crime,"crime","ogr")
processing.run("qgis:joinattributesbylocation",{'DISCARD_NONMATCHING' : False, 'INPUT' : districts, 'JOIN' : crime, 'JOIN_FIELDS' : [], 'METHOD' : 0, 'OUTPUT' : 'S:/682/Spring20/rburns12\Labs\Lab4\Data\joined.shp', 'PREDICATE' : [1], 'PREFIX' : '' })
join = "S:/682/Spring20/rburns12/Labs/Lab4/Data/joined.shp" 
iface.addVectorLayer(join,"join","ogr") 
#The DC police district that had the most crimes was District 3, which had 5970 crimes reported.
