'''
Created on Oct 12, 2012

@author: npanta2
'''

import unittest
import sourcecode.Parser
import gui.Part2Methods
import sourcecode.PublicVariables

class testCost(unittest.TestCase):
    
    sourcecode.Parser
    '''   
    def testTwoCities(self):
        gui.Part2Methods.routeInformation()
        self.assertEquals(sourcecode.PublicVariables.finalCities, "MEX --> MIA --> end")
        self.assertEquals(sourcecode.PublicVariables.distance, 2053)
        self.assertEquals(sourcecode.PublicVariables.cost, 718.55)
        self.assertEquals(sourcecode.PublicVariables.time, 3.270666666666667)
    '''  
    def testThreeCities(self):
        gui.Part2Methods.routeInformation()
        self.assertEquals(sourcecode.PublicVariables.finalCities, "MEX --> MIA --> ATL --> end")
        self.assertEquals(sourcecode.PublicVariables.distance, 3010)
        self.assertEquals(sourcecode.PublicVariables.cost, 1005.6499999999999)
        self.assertEquals(sourcecode.PublicVariables.time, 6.617333333333334)