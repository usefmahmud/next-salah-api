import salat
import datetime
import pytz
from .location import Location
from typing import Dict, List


class Salah:

    def __init__(
        self,
        geo_coords: tuple,
        timezone: str,
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
                'name': name.capitalize(),
                'time': time.strftime('%H:%M')
            } for name, time in prayer_times.items()
        ]

    def get_prev_next_salah(self) -> Dict[str, Dict[str, str]]:
        '''
        Get the previous and next salah times.
        '''
        all_salah = self.get_all_salah(datetime.date.today())
        current_time = datetime.datetime.now(self.timezone).time()

        next_salah = None
        next_salah_idx = -1

        for salah in all_salah:
            salah_time = datetime.datetime.strptime(salah['time'], '%H:%M').time()

            salah_seconds = salah_time.hour * 3600 + salah_time.minute * 60 + salah_time.second
            current_seconds = current_time.hour * 3600 + current_time.minute * 60 + current_time.second
            print(current_seconds, salah_seconds)
            if current_seconds < salah_seconds:
                next_salah = salah
                next_salah_idx += 1
                break
            else:
                next_salah_idx += 1

        # If the current time is after the last salah, the next salah is the first salah of the next day
        # and the previous salah is the last salah of the current day.
        return {
            'previous': all_salah[next_salah_idx - 1] if next_salah_idx > 0 else all_salah[-1],
            'next': next_salah if next_salah else all_salah[0]
        }


# Testing the Salah class
location = Location('Cairo, Egypt')
salah = Salah(location.geo_coords(), 'Africa/Cairo')
print(salah.get_prev_next_salah())
