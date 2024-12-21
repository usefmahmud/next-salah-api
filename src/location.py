from geopy.geocoders import Nominatim


class Location:
    def __init__(self, address: str):
        self.address = address

    def get_lat_long(self) -> tuple:
        '''
        Get the latitude and longitude of a location using the address.
        '''

        geolocator = Nominatim(user_agent='next-salah-api')
        loc = geolocator.geocode(self.address)

        return (loc.latitude, loc.longitude)
