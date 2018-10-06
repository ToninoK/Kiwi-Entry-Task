class Option:
    
    def __init__(self, data):
        self.data = data

    def structure_cities(self):
        lst = []
        for airport in self.data['locations']:
            airport_cities_data = []
            airport_cities_data.append(airport['name'])
            airport_cities_data.append(airport['city']['name'])
            lst.append(airport_cities_data)
        return lst

    def structure_coords(self):
        lst = []
        for airport in self.data['locations']:
            airport_cities_data = []
            airport_cities_data.append(airport['name'])
            airport_cities_data.append(airport['location']['lon'])
            airport_cities_data.append(airport['location']['lat'])
            lst.append(airport_cities_data)
        return lst

    def structure_iata(self):
        lst = []
        for airport in self.data['locations']:
            airport_cities_data = []
            airport_cities_data.append(airport['code'])
            airport_cities_data.append(airport['name'])
            lst.append(airport_cities_data)
        return lst
    
    def structure_names(self):
        lst = []
        for airport in self.data['locations']:
            airport_cities_data = []
            airport_cities_data.append(airport['name'])
            lst.append(airport_cities_data)
        return lst
    
    def structure_full(self):
        lst = []
        for airport in self.data['locations']:
            airport_cities_data = []
            airport_cities_data.append(airport['code'])
            airport_cities_data.append(airport['name'])
            airport_cities_data.append(airport['city']['name'])
            airport_cities_data.append(airport['location']['lon'])
            airport_cities_data.append(airport['location']['lat'])
            lst.append(airport_cities_data)
        return lst
    
    def structure_option_free(self):
        lst = []
        for airport in self.data['locations']:
            airport_cities_data = []
            airport_cities_data.append(airport['code'])
            airport_cities_data.append(airport['name'])
            lst.append(airport_cities_data)
        return lst