'''
Created on Oct 12, 2012

@author: npanta2
'''

import sourcecode.PublicVariables
import webbrowser

#helper function for printAllAvailableCities
def getCities(city):
    connectedList = ""
    for key in sourcecode.PublicVariables.cityList.get(city).routes.keys():
        connectedList = connectedList + city + "-" + key + ","
    return connectedList

#prints all cities and codes in JSON data
def printAllAvailableCities():
    for key in sourcecode.PublicVariables.cityList.keys():
        print sourcecode.PublicVariables.cityList.get(key).name + " - " + key

#opens webbrowser and maps cities routes using gcmap.com
def printMapCities(input):    
    for key in sourcecode.PublicVariables.cityList.keys():
        if input.upper() == key:
            cities = getCities(input)
    url = 'http://www.gcmap.com/mapui?P=' + cities
    webbrowser.open_new_tab(url)

#print city information
def printCityInformation(key, input):
    if input.upper() == key:
        print "Code: " + key
        print "Name: " + sourcecode.PublicVariables.cityList.get(key).name
        print "Country: " + sourcecode.PublicVariables.cityList.get(key).country
        print "Continent: " + sourcecode.PublicVariables.cityList.get(key).continent
        print "Timezone: ", sourcecode.PublicVariables.cityList.get(key).timezone
        for coord in sourcecode.PublicVariables.cityList.get(key).coordinates.keys():
            print coord + ": ", sourcecode.PublicVariables.cityList.get(key).coordinates.get(coord), "degrees"
        print "Population: ", sourcecode.PublicVariables.cityList.get(key).population
        print "Region: ", sourcecode.PublicVariables.cityList.get(key).region
        print "Routes:"
        for route in sourcecode.PublicVariables.cityList.get(key).routes.keys():
            print route, sourcecode.PublicVariables.cityList.get(key).routes.get(route).distance

#print required statistics 
def printStats():
    numOfCities = 0
    currHubCity = 0
    
    #calculate longest, shortest, and average flight along with hub cities
    for key in sourcecode.PublicVariables.cityList.keys():
        newHubCity = 0
        for route in sourcecode.PublicVariables.cityList.get(key).routes.keys():
            if sourcecode.PublicVariables.longestFlight == 0 or sourcecode.PublicVariables.longestFlight < sourcecode.PublicVariables.cityList.get(key).routes.get(route).distance:
                sourcecode.PublicVariables.longestFlight = sourcecode.PublicVariables.cityList.get(key).routes.get(route).distance
            if sourcecode.PublicVariables.shortestFlight == 0 or sourcecode.PublicVariables.shortestFlight > sourcecode.PublicVariables.cityList.get(key).routes.get(route).distance:
                sourcecode.PublicVariables.shortestFlight = sourcecode.PublicVariables.cityList.get(key).routes.get(route).distance
            newHubCity += 1
        if currHubCity == 0 or currHubCity < newHubCity:
            sourcecode.PublicVariables.hubCities = sourcecode.PublicVariables.cityList.get(key).name
            currHubCity = newHubCity
        if currHubCity == 0 or currHubCity == newHubCity:
            sourcecode.PublicVariables.hubCities += ", " + sourcecode.PublicVariables.cityList.get(key).name
        sourcecode.PublicVariables.averageDistance += sourcecode.PublicVariables.cityList.get(key).routes.get(route).distance
        numOfCities += 1 
    sourcecode.PublicVariables.averageDistance = sourcecode.PublicVariables.averageDistance / numOfCities     
    print "Longest Flight: " + str(sourcecode.PublicVariables.longestFlight)
    print "Shortest Flight: " + str(sourcecode.PublicVariables.shortestFlight)
    print "Average Flight: " + str(sourcecode.PublicVariables.averageDistance)
    print "Hub City: " + sourcecode.PublicVariables.hubCities +  " = " + str(currHubCity)         
    
    #calculate biggest, smallest, and average city population
    for key in sourcecode.PublicVariables.cityList.keys():
        if sourcecode.PublicVariables.biggestCityPop == 0 or sourcecode.PublicVariables.biggestCityPop < sourcecode.PublicVariables.cityList.get(key).population:
            sourcecode.PublicVariables.biggestCityPop = sourcecode.PublicVariables.cityList.get(key).population
        if sourcecode.PublicVariables.smallestCityPop == 0 or sourcecode.PublicVariables.smallestCityPop > sourcecode.PublicVariables.cityList.get(key).population:
            sourcecode.PublicVariables.smallestCityPop = sourcecode.PublicVariables.cityList.get(key).population
        sourcecode.PublicVariables.averageCityPop += sourcecode.PublicVariables.cityList.get(key).population
        #numOfCities += 1   
    sourcecode.PublicVariables.averageCityPop = sourcecode.PublicVariables.averageCityPop / numOfCities         
    print "Biggest Population: " + str(sourcecode.PublicVariables.biggestCityPop)
    print "Smallest Population: " + str(sourcecode.PublicVariables.smallestCityPop)
    print "Average Population: " + str(sourcecode.PublicVariables.averageCityPop)
