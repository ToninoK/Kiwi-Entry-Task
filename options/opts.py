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
        airport_cities_data = []
        for airport in self.data:
            airport_cities_data.append(airport['city']['name'])
        return airport_cities_data

    def structure_coords(self):
        """Function which returns a list of data for the airports

        Returns:
            list -- contains airport data; longitude, lattitude
        """
    
        lst = []
        airport_longitudes = []
        airport_latitudes = []
        for airport in self.data:
            airport_longitudes.append(airport['location']['lon'])
            airport_latitudes.append(airport['location']['lat'])
        lst.append(airport_longitudes)
        lst.append(airport_latitudes)
        return lst

    def structure_iata(self):
        """Function which returns a list of data for the airports

        Returns:
            list -- contains airport data; iata code
        """
        airport_iata_data = []
        for airport in self.data:
            airport_iata_data.append(airport['code'])
        return airport_iata_data
    
    def structure_names(self):
        """Function which returns a list of data for the airports

        Returns:
            list -- contains airport data; name
        """

        airport_name_data = []
        for airport in self.data:
            airport_name_data.append(airport['name'])
        return airport_name_data
    
    def structure_full(self):
        """Function which returns a list of data for the airports

        Returns:
            list -- contains airport data; iata code, name, city, longitude, lattitude
        """

        lst = []
        for airport in self.data:
            airport_full_data = []
            airport_full_data.append(airport['code'])
            airport_full_data.append(airport['name'])
            airport_full_data.append(airport['city']['name'])
            airport_full_data.append(airport['location']['lon'])
            airport_full_data.append(airport['location']['lat'])
            lst.append(airport_full_data)
        return lst
    
    def structure_option_free(self):
        """Function which returns a list of data for the airports

        Returns:
            list -- contains airport data; iata code, name
        """

        lst = []
        for airport in self.data:
            airport_optfree_data = []
            airport_optfree_data.append(airport['code'])
            airport_optfree_data.append(airport['name'])
            lst.append(airport_optfree_data)
        return lst