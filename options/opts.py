class Option:
    """
    Class that holds the function needed for each arguments' output handling
    """
    
    def __init__(self, data):
        """Init function for the Option class

        Arguments:
            data {dict}:
            {
                "locations": list,
                "meta": dict
            }
        """
        self.data = data['locations']

    def structure_cities(self):
        """Function which returns a list of data for the airports

        Returns:
            list -- contains airport data; name, city
        """

        lst = []
        for airport in self.data:
            airport_cities_data = []
            airport_cities_data.append(airport['name'])
            airport_cities_data.append(airport['city']['name'])
            lst.append(airport_cities_data)
        return lst

    def structure_coords(self):
        """Function which returns a list of data for the airports

        Returns:
            list -- contains airport data; name, longitude, lattitude
        """
    
        lst = []
        for airport in self.data:
            airport_cities_data = []
            airport_cities_data.append(airport['name'])
            airport_cities_data.append(airport['location']['lon'])
            airport_cities_data.append(airport['location']['lat'])
            lst.append(airport_cities_data)
        return lst

    def structure_iata(self):
        """Function which returns a list of data for the airports

        Returns:
            list -- contains airport data; iata code, name
        """
        lst = []
        for airport in self.data:
            airport_cities_data = []
            airport_cities_data.append(airport['code'])
            airport_cities_data.append(airport['name'])
            lst.append(airport_cities_data)
        return lst
    
    def structure_names(self):
        """Function which returns a list of data for the airports

        Returns:
            list -- contains airport data; name
        """

        lst = []
        for airport in self.data:
            airport_cities_data = []
            airport_cities_data.append(airport['name'])
            lst.append(airport_cities_data)
        return lst
    
    def structure_full(self):
        """Function which returns a list of data for the airports

        Returns:
            list -- contains airport data; iata code, name, city, longitude, lattitude
        """

        lst = []
        for airport in self.data:
            airport_cities_data = []
            airport_cities_data.append(airport['code'])
            airport_cities_data.append(airport['name'])
            airport_cities_data.append(airport['city']['name'])
            airport_cities_data.append(airport['location']['lon'])
            airport_cities_data.append(airport['location']['lat'])
            lst.append(airport_cities_data)
        return lst
    
    def structure_option_free(self):
        """Function which returns a list of data for the airports

        Returns:
            list -- contains airport data; iata code, name
        """

        lst = []
        for airport in self.data:
            airport_cities_data = []
            airport_cities_data.append(airport['code'])
            airport_cities_data.append(airport['name'])
            lst.append(airport_cities_data)
        return lst