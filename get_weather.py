"""This is a command line program that will retrieve info on the current 
weather from a city that the user inputs. The program uses the API from 
openweathermap.org.
"""

from urllib2 import urlopen, URLError
from json import load 

def main():
    try:
        url = "http://openweathermap.org/data/2.5/weather?q="
        city = raw_input("Enter the city whose current weather you want to see: ")
        api_key = "&APPID=3b8fff5eb8a9347bd1d613d5c3d0af2d"
        url += city + "&units=imperial" + api_key

        response = urlopen(url)
        json_obj = load(response)

        proper_city_name = json_obj[u'name']
        weather_description = json_obj[u'weather'][0][u'description']
        main_lookup = json_obj[u'main']
        humidity = int(main_lookup[u'humidity'])
        temp = int(main_lookup[u'temp'])
        low_temp = int(main_lookup[u'temp_min'])
        high_temp = int(main_lookup[u'temp_max'])

        print "Weather for %s: %s" % (proper_city_name, weather_description) + "."
        print "Humidity: %d percent." % humidity
        print "Current temperature: %d degrees Fahrenheit (high of %d, low of %d)." % (temp, low_temp, high_temp)
    except URLError, e:
        print "Got error code ", e

if __name__ == "__main__":
    main()