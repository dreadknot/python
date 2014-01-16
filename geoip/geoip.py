import GeoIP 

gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE) 
gi = GeoIP.open("/usr/share/GeoIP/GeoLiteCity.dat",GeoIP.GEOIP_STANDARD) 

print '<?xml version="1.0" encoding="UTF-8"?>' 
print '<kml xmlns="http://www.opengis.net/kml/2.2">' 
print '<Document>' 

 

for line in file("ips.txt", "r"): 
    line = line[:-1] # strip the last from the line 
    gir = gi.record_by_addr(line) 
    print "<Placemark>" 
    print "<name>", line, "</name>" 
    print "<Point>" 
    print '<coordinates>%s, %s, 0</coordinates>' % (gir['longitude'], gir['latitude']) 
#    print "<coordinates>",gir['longitude'],",",gir['latitude'],", 0", "</coordinates>" 
    print "</Point>" 
    print "</Placemark>" 


print '</Document>' 
print "</kml>" 