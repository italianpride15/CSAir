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
    gui.Part2Methods.commitChanges()
    
    def testIfData(self):
        assert(sourcecode.PublicVariables.data)
        
