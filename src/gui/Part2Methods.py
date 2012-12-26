'''
Created on Oct 12, 2012

@author: npanta2
'''

import sourcecode.PublicVariables
import json
import sourcecode.Cities_List
import sourcecode.Routes_List
import sourcecode.Cost

#main menu for editing route network
def editRouteNetwork():
    print "Press 1 to remove a city from CSAir route network"
    print "Press 2 to remove a route from CSAir route network"
    print "Press 3 to add a city to CSAir route network"
    print "Press 4 to add a route to CSAir route network"
    print "Press 5 to edit existing city"
    input = raw_input("> ")
    
    if input == "1":
        print "Enter city code to be removed"
        input = raw_input("> ")
        removeCity(input.upper())

    if input == "2":
        removeRoute()

    if input == "3":
        print "Enter a city and information in the following order. Press enter after each item: code, name, country, continent, timezone, coordinates, population, region"
        addCity()

    if input == "4":
        print "Enter route and distance in the following format. Press enter after each item: start city code, end city code, distance"
        addRoute()

    if input == "5":
        print "Enter city code to be edited"
        input = raw_input("> ")
        editCity(input.upper())

#remove a city - will also validate city
def removeCity(input):
    if sourcecode.PublicVariables.cityList.has_key(input) == False:
        print "City not in CSAir's records"
    else:
        removeRouteCity(input)
        sourcecode.PublicVariables.cityList.pop(input)
        
#helper function for removeCity - removes all city's associated routes
def removeRouteCity(input):
    for key in sourcecode.PublicVariables.cityList.get(input).routes.keys():
        sourcecode.PublicVariables.cityList.get(key).routes.pop(input)

#remove a route from JSON data
def removeRoute():
    print "Enter city to remove route from"
    city = raw_input("> ")
    print "Enter route to remove"
    route = raw_input("> ")
    sourcecode.PublicVariables.cityList.get(city).routes.pop(route)

#add city to citylist
def addCity():
    #get info
    print "City Code:"
    input = raw_input("> ")
    code = input
    print "City Name:"
    input = raw_input("> ")
    name = input
    print "Country:"
    input = raw_input("> ")
    country = input
    print "Continent:"
    input = raw_input("> ")
    continent = input
    print "Timezone:"
    input = int(raw_input("> "))
    timezone = input
    print "Coordinates:"
    print "N or S"
    input = raw_input("> ")
    while input.upper() != "N" and input.upper() != "S":
        print "N or S:"
        input = raw_input("> ")
    NorS = input
    print "Enter coordinate:"
    input = int(raw_input("> "))
    while input < 0:
         print "Enter coordinate:"
         input = int(raw_input("> "))
    NorSCoord = input 
    print "E or W"
    input = raw_input("> ")
    while input.upper() != "E" and input.upper() != "W":
        print "E or W:"
        input = raw_input("> ")
    EorW = input
    print "Enter coordinate:"
    input = int(raw_input("> "))
    while input < 0:
         print "Enter coordinate:"
         input = int(raw_input("> "))
    EorWCoord = input
    coordinates = {NorS : NorSCoord, EorW : EorWCoord}
    print coordinates
    print "Population:"
    input = int(raw_input("> "))
    while input < 0:
        print "Population:"
        input = int(raw_input("> "))
    population = input
    print "Region:"
    input = int(raw_input("> "))
    region = input
    #add city
    newCity = sourcecode.Cities_List.Cities_List(code, name, country, continent,
                                                 timezone, coordinates, population,
                                                 region)
        
    sourcecode.PublicVariables.cityList[code] = newCity
    
#add new route to city in citylist 
def addRoute():
    print "Add first City Code:"
    city1 = raw_input("> ")
    print "Add second City Code:"
    city2 = raw_input("> ")
    print "Add distance between cities:"
    distance = int(raw_input("> "))
    #setting both cities route dictionaries
    newRoute1 = sourcecode.Routes_List.Routes_List(city1, distance)
    sourcecode.PublicVariables.cityList.get(city2).routes[city1] = newRoute1
    newRoute2 = sourcecode.Routes_List.Routes_List(city2, distance)
    sourcecode.PublicVariables.cityList.get(city1).routes[city2] = newRoute2

#edit a city in citylist          
def editCity(input):
    myCode = input
    while input != "done":
        print "What do you want to edit?"
        print "1 - name, 2 - country, 3 - continent, 4 - timezone, 5 - coordinates, 6 - population, 7 - region, 'done' to commit this change"
        input = raw_input("> ")        
        if input == "1":
            print "Enter name:"
            input = raw_input("> ")
            sourcecode.PublicVariables.cityList.get(myCode).name = input 
        if input == "2":
            print "Enter country:"
            input = raw_input("> ")
            sourcecode.PublicVariables.cityList.get(myCode).country = input
        if input == "3":
            print "Enter continent:"
            input = raw_input("> ")
            sourcecode.PublicVariables.cityList.get(myCode).continent = input
        if input == "4":
            print "Enter timezone:"
            input = int(raw_input("> "))
            sourcecode.PublicVariables.cityList.get(myCode).timezone = input 
        if input == "5":
            print "Coordinates:"
            print "N or S"
            input = raw_input("> ")
            while input.upper() != "N" and input.upper() != "S":
                print "N or S:"
                input = raw_input("> ")
            NorS = input
            print "Enter coordinate:"
            input = int(raw_input("> "))
            while input < 0:
                 print "Enter coordinate:"
                 input = int(raw_input("> "))
            NorSCoord = input 
            print "E or W"
            input = raw_input("> ")
            while input.upper() != "E" and input.upper() != "W":
                print "E or W:"
                input = raw_input("> ")
            EorW = input
            print "Enter coordinate:"
            input = int(raw_input("> "))
            while input < 0:
                 print "Enter coordinate:"
                 input = int(raw_input("> "))
            EorWCoord = input
            coordinates = {NorS : NorSCoord, EorW : EorWCoord}
            sourcecode.PublicVariables.cityList.get(myCode).coordinates = input
        if input == "6":
            print "Enter population:"
            input = int(raw_input("> "))
            while input < 0:
                print "Enter population:"
                input = int(raw_input("> "))
            sourcecode.PublicVariables.cityList.get(myCode).population = int(input)
        if input == "7":
            print "Enter region:"
            input = int(raw_input("> "))
            while input < 0:
                print "Enter region:"
                input = int(raw_input("> "))
            sourcecode.PublicVariables.cityList.get(myCode).region = input        

#saves changes made to json file in map_data.json
def commitChanges():
    data = {}
    metro = []
    routes = []
    #format each key in citylist
    for key in sourcecode.PublicVariables.cityList.keys():    
        node = {}
        node["code"] = key
        node["name"] = sourcecode.PublicVariables.cityList.get(key).name
        node["country"] = sourcecode.PublicVariables.cityList.get(key).country
        node["continent"] = sourcecode.PublicVariables.cityList.get(key).continent
        node["timezone"] = sourcecode.PublicVariables.cityList.get(key).timezone
        node["coordinates"] = sourcecode.PublicVariables.cityList.get(key).coordinates
        node["population"] = sourcecode.PublicVariables.cityList.get(key).population
        node["region"] = sourcecode.PublicVariables.cityList.get(key).region
        metro.append(node)
        #format each route in city
        for route in sourcecode.PublicVariables.cityList.get(key).routes.keys():
            rnode = {}
            rt = []
            rt.append(key)
            rt.append(route)
            rnode["ports"] = rt
            rnode["distance"] = sourcecode.PublicVariables.cityList.get(key).routes.get(route).distance
            routes.append(rnode)
    #write the newly formatted data to the file
    data["data sources"] = sourcecode.PublicVariables.sourceList
    data["metros"] = metro
    data["routes"] = routes
    json.dump(data, open('map_data.json', 'w'), indent=4)

#get route information - see Cost class
def routeInformation():
    cost = sourcecode.Cost.Cost()
    while True:
        print "Enter City code:" 
        city = raw_input("> ")
        if city.lower() == "quit":
            break
        if city.lower() == "done":
            if len(cost.pathlist) < 1:
                print "Need more cities. Please restart."
                break
            cost.printCosts()
            cost.getLayoverTime()
            break
        cost.addCity(city)
           
