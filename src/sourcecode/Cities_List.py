'''

@author: npanta2
'''

class Cities_List:
    
    def __init__(self, code,
                       name,
                       country,
                       continent,
                       timezone,
                       coordinates,
                       population,
                       region):
    
        self.name = name
        self.country = country
        self.continent = continent
        self.timezone = timezone
        self.coordinates = coordinates
        self.population = population
        self.region = region
        self.routes = {}
        
    #self.routes = routes


    