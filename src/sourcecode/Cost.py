'''
Created on Oct 12, 2012

@author: npanta2
'''
 
import PublicVariables
import math
   
class Cost: 
    
    #make an instance each time
    def __init__(self): 
        self.pathlist = []
        self.distance = 0
        self.cost = 0
        self.time = 0.0
        self.costperkm = .35
    
    #adds a city to pathlist
    def addCity(self, city):
        self.pathlist.append(city) 
        if len(self.pathlist) > 1:
            length = len(self.pathlist) - 2
            self.calculateCosts(str(self.pathlist[length]), city)
            if self.costperkm > 0:
                self.costperkm -= .05  
     
    #calculates costs on the fly       
    def calculateCosts(self, city1, city2):
            self.distance += PublicVariables.cityList.get(city1).routes.get(city2).distance
            self.cost += self.costperkm * PublicVariables.cityList.get(city1).routes.get(city2).distance
            self.calculateTime()

    #calculates time on the fly
    def calculateTime(self):
        tempDistance = self.distance
        if tempDistance >= 400:
            tempDistance -= 400.0
            tempDistance = tempDistance/750.0
            accelerationTime = (400.0 / 750.0) * 2
            self.time += accelerationTime + tempDistance
        else: #<400
            self.time += 2 * math.sqrt(tempDistance / math.pow(750, 2) / 400)
    
    #calculates layovertime when called from driver        
    def getLayoverTime(self):
        counter = 0
        layoverTime = 2
        for key in self.pathlist:
            if counter > 0 and counter < (len(self.pathlist)-1):
                lenght = len(PublicVariables.cityList.get(key).routes)
                layoverTime -= lenght * (1 * .16)
            counter += 1
        if layoverTime != 2:
            self.time -= layoverTime
     
    #prints out cost details when called from driver       
    def printCosts(self):
        self.getLayoverTime()
        i = 0
        finalString = ""
        for key in self.pathlist:
            finalString += self.pathlist[i] + " --> "
            i += 1
        finalString += "end"
        PublicVariables.finalCities = finalString
        PublicVariables.distance = self.distance
        PublicVariables.cost = self.cost
        PublicVariables.time = self.time
        print finalString
        print "Distance: " + str(self.distance)
        print "Cost: $" + str(self.cost)
        print "Time: " + str(self.time) + " hours"

