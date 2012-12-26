'''

@author: npanta2
'''
import unittest
import sourcecode.Parser

class testCities(unittest.TestCase):

    sourcecode.Parser

    def testCMI(self):
        key = sourcecode.PublicVariables.cityList.has_key("CMI")
        self.assertEqual(key, True)
        
    def testCMIData(self):
        key = sourcecode.PublicVariables.cityList.get("CMI").population
        self.assertEqual(key, 226000)
        key1 = sourcecode.PublicVariables.cityList.get("CMI").region
        self.assertEqual(key1, 1)
        
    def testName(self):
        key = sourcecode.PublicVariables.cityList.keys()[0]
        self.assertEquals(key, "PAR")

    def testSize(self):
        print len(sourcecode.PublicVariables.cityList)
        self.assertEquals(len(sourcecode.PublicVariables.cityList), 49)
        
    def testCountry(self):
        key = sourcecode.PublicVariables.cityList.get("SCL")
        self.assertEquals(key.name, "Santiago")
        
    def testContinent(self):
        key = sourcecode.PublicVariables.cityList.get("LIM")
        self.assertEquals(key.continent, "South America")
        
    def testTimezone(self):
        key = sourcecode.PublicVariables.cityList.get("MEX")
        self.assertEquals(key.timezone, -6)
        
    def testCoordinates(self):
        key = sourcecode.PublicVariables.cityList.get("BUE")
        #self.assertEquals("S:  35 degrees\nW:  58 degrees", , msg)
        
    def testPopulation(self):
        key = sourcecode.PublicVariables.cityList.get("SAO")
        self.assertEquals(key.population, 20900000)
        
    def testRegion(self):
        key = sourcecode.PublicVariables.cityList.get("LOS")
        self.assertEquals(key.region, 1)
        
    def testRoutes(self):
        key = sourcecode.PublicVariables.cityList.get("JNB")
        #implement

        


