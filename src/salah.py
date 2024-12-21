import salat
import datetime
import pytz
from location import Location
from typing import Dict, List


class Salah:

    def __init__(
        self,
        geo_coords: tuple,
        timezone,
        method: salat.CalculationMethod = salat.CalculationMethod.EGYPT
    ):
        if not isinstance(geo_coords, tuple) or len(geo_coords) != 2:
            raise ValueError('geo_coords must be a tuple of (longitute, latitude).')

        self.long = geo_coords[0]
        self.lat = geo_coords[1]

        if not isinstance(timezone, str):
            raise ValueError("timezone must be a valid timezone string.")

        try:
            self.timezone = pytz.timezone(timezone)
        except pytz.UnknownTimeZoneError:
            raise ValueError(f"Unknown timezone: {timezone}")

        self.calc_method = method

    def get_all_salah(self, date: datetime.date) -> List[Dict[str, str]]:
        '''
        Get all the salah times for the day.

        :param date: Date for which to calculate the prayer times.
        :return: A list of prayer names and their times.
        '''
        pt = salat.PrayerTimes(self.calc_method)
        prayer_times = pt.calc_times(
                date,
                self.timezone,
                self.long, self.lat
            )

        return [
            {
                'name': name,
                'time': time.strftime('%H:%M')
            } for name, time in prayer_times.items()
        ]

    def get_prev_next_salah(self):
        '''
        Get the previous and next salah times.
        '''
        pass


# Testing the Salah class
location = Location('Cairo, Egypt')
salah = Salah(location.get_lat_long(), 'Africa/Cairo')
print(salah.get_all_salah(datetime.date.today()))
