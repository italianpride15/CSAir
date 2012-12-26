'''

@author: npanta2
'''
import unittest
import sourcecode.Parser
import sourcecode.PublicVariables
import gui.Driver

longestFlight = 12051
shortestFlight = 132
averageFlight = 2550
biggestCityPop = 34000000
smallestCityPop = 226000
averageCityPop = 11560018
continentsAndCities = ""
hubCities = u'Champaign, Champaign'

class Test(unittest.TestCase):
    
    sourcecode.Parser
    gui.Part1Methods.printStats()
    
    def testLongestFlight(self):
        self.assertEquals(longestFlight, sourcecode.PublicVariables.longestFlight)
        
    def testShortestFlight(self):
        self.assertEquals(shortestFlight, sourcecode.PublicVariables.shortestFlight)
        
    def testAvgDistance(self):
        self.assertEquals(averageFlight, sourcecode.PublicVariables.averageDistance)
        
    def testBiggestCityPop(self):
        self.assertEquals(biggestCityPop, sourcecode.PublicVariables.biggestCityPop)
        
    def testSmallCityPop(self):
        self.assertEquals(smallestCityPop, sourcecode.PublicVariables.smallestCityPop)
        
    def testavgCityPop(self):
        self.assertEquals(averageCityPop, sourcecode.PublicVariables.averageCityPop)
        
    def testHubCities(self):
        self.assertEquals(hubCities, sourcecode.PublicVariables.hubCities)
        
        