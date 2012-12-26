'''

@author: npanta2
'''

    
import Cities_List
import Routes_List
import Continents
import PublicVariables
import json
import urllib

#URL strings for automatic loading
URL1 = "https://wiki.engr.illinois.edu/download/attachments/207295743/map_data.json?version=1&modificationDate=1349245462000"
URL2 = "https://wiki.engr.illinois.edu/download/attachments/207295743/cmi_hub.json?version=1&modificationDate=1349245386000"

#helper function - parsing json and adding new sources
def addSources(data):
    i = 0
    for key in data["data sources"]:
        PublicVariables.sourceList.append(data["data sources"][i])
        i += 1
    
#helper function - parsing json and adding new city to dictionary
def addCities(data):
    for key in data["metros"]:
        newCity = Cities_List.Cities_List(key["code"],
                                          key["name"],
                                          key["country"],
                                          key["continent"],
                                          key["timezone"],
                                          key["coordinates"],
                                          key["population"],
                                          key["region"])
        
        PublicVariables.cityList[key["code"]] = newCity
 
#helper function - parsing json and adding routes to cities       
def addRoutes(data):
    for key in data["routes"]:
        newRoute1 = Routes_List.Routes_List(key["ports"][0], key["distance"])
        PublicVariables.cityList.get(key["ports"][1]).routes[key["ports"][0]] = newRoute1  
        newRoute2 = Routes_List.Routes_List(key["ports"][1], key["distance"])
        PublicVariables.cityList.get(key["ports"][0]).routes[key["ports"][1]] = newRoute2

#helper function - adding countries to continents
def addContinents(data):
    for key in PublicVariables.cityList.keys():   
        if PublicVariables.cityList.get(key).continent == "North America":  
            PublicVariables.northAmerica[key["code"]] = key
        if PublicVariables.cityList.get(key).continent == "South America":   
            PublicVariables.southAmerica[key["code"]] = key  
        if PublicVariables.cityList.get(key).continent == "Asia":     
            PublicVariables.asia[key["code"]] = key
        if PublicVariables.cityList.get(key).continent == "Europe":   
            PublicVariables.europe[key["code"]] = key
        if PublicVariables.cityList.get(key).continent == "Africa":   
            PublicVariables.africa[key["code"]] = key
        if PublicVariables.cityList.get(key).continent == "Australia":  
            PublicVariables.australia[key["code"]] = key
        if PublicVariables.cityList.get(key).continent == "Antartica":              
            PublicVariables.antartica[key["code"]] = key
            
class Parser: 
  
    #get json file
    print "Press 1 to load JSON files automatically. Press 2 to load JSON files manually."
    input = raw_input("> ")
    
    #automatically load files
    if input == "1":
        file = urllib.urlopen(URL1).read()
        PublicVariables.data = json.loads(file)

        #process data
        addSources(PublicVariables.data)
        addCities(PublicVariables.data)
        addRoutes(PublicVariables.data)
        #addContinents(data)
        
        file = urllib.urlopen(URL2).read()
        PublicVariables.data = json.loads(file)

        #process data
        addSources(PublicVariables.data)
        addCities(PublicVariables.data)
        addRoutes(PublicVariables.data)
        #addContinents(data)
        
    #explicitly select files to load using URL
    if input == "2":
        while input != "done":
            print "Paste URL for JSON File"
            input = raw_input("> ")
            if input != "done":
                file = urllib.urlopen(input).read()
                PublicVariables.data = json.loads(file)

                #process data
                addSources(PublicVariables.data)
                addCities(PublicVariables.data)
                addRoutes(PublicVariables.data)
                #addContinents(data)

        
        