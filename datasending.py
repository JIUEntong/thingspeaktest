
import urllib

from bs4 import BeautifulSoup

data=urllib.urlopen("https://api.thingspeak.com/update?api_key=D396MCBYBEFWFBG6&field1=0"+str(500));
print data;
