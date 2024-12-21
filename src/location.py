from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder


class Location:
    def __init__(self, address: str):
        self.address = address

    def geo_coords(self) -> tuple:
        '''
        Get the latitude and longitude of a location using the address.
        '''

        geolocator = Nominatim(user_agent='next-salah-api')
        loc = geolocator.geocode(self.address)

        return (loc.longitude, loc.latitude)

    def timezone(self) -> str:
        '''
        Get the timezone of a location using the latitude and longitude.
        '''

        tf = TimezoneFinder()
        return tf.timezone_at(lat=self.get_lat_long()[0], lng=self.get_lat_long()[1])
