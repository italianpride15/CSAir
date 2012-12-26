'''
Created on Oct 12, 2012

@author: npanta2
'''

import unittest
import sourcecode.Parser
import sourcecode.PublicVariables
import gui.Part2Methods

class testData(unittest.TestCase):
    
    sourcecode.Parser

    def testRemoveCity(self):
        gui.Part2Methods.removeCity("PAR")
        self.assertFalse(sourcecode.PublicVariables.cityList.has_key("PAR"))
      
    def testRemoveRoute(self):
        gui.Part2Methods.removeRoute() #MEX, MIA
        gui.Part2Methods.commitChanges()
    
    def testAddCity(self):
        gui.Part2Methods.addCity()
        self.assertTrue(sourcecode.PublicVariables.cityList.has_key("FAN"))

    def testAddRoute(self):
        gui.Part2Methods.addRoute() #MEX, LON, 0
        gui.Part2Methods.commitChanges()

    def testEditCity(self):
        gui.Part2Methods.editCity("CMI") #press 1 - hello
        self.assertEquals(sourcecode.PublicVariables.cityList.get("CMI").name, "hello")
      