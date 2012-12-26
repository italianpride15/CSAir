'''

@author: npanta2
'''
import sourcecode.Parser
import sourcecode.PublicVariables
import Part2Methods
import Part1Methods

#helper function for "map"


class Driver:
    
    #parse json
    sourcecode.Parser
    
    #Get User input. Bad input will just restart
    while True:
        print "Press 1 to enter CSAir menu 2.0"
        print "Press 2 to enter CSAir menu 2.1"
        print "Type 'quit' at any time to quit"
        input = raw_input("> ")

        if input.lower() == "quit":
                print "Thank You for using CSAir."
                break
            
        #enter old menu
        if input.lower() == "1":
            
            print "Type 'all' to get a list of all available CSAir cities"
            print "Type the city name to get information about the city"
            print "Type 'stats' to get statistical information about CSAir's route network"
            print "Type 'map' if you would you like to map your route"
            input = raw_input("> ")

            #print out all available cities and codes
            if input.lower() == "all":
                Part1Methods.printAllAvailableCities()
                  
            #SHOULD I PRINT THE CITY TOO?
            #display all statistical data
            if input.lower() == "stats":
                Part1Methods.printStats()
                
            #open webbrowser to gcmap.com with selected city name
            if input.lower() == "map":
                print "Type in the city's code"
                input = raw_input(">> ")
                Part1Methods.printMapCities(input)
                
            if input.lower() == "quit":
                print "Thank You for using CSAir."
                break
    
            #else check if typed in a city to look up info
            for key in sourcecode.PublicVariables.cityList.keys():
                Part1Methods.printCityInformation(key, input)
        
        #enter new menu
        if input == "2":
            
            print "Type 'edit' to edit CSAir's route network"
            print "Type 'commit' to commit changes to CSAir's route network"
            print "Type 'route' to get information about your route"
            input = raw_input("> ")
            
            if input.lower() == "edit":
                Part2Methods.editRouteNetwork()
            
            if input.lower() == "commit":
                Part2Methods.commitChanges()
            
            if input.lower() == "route":
                Part2Methods.routeInformation()
                  
            if input.lower() == "quit":
                print "Thank You for using CSAir."
                break

            
            
                