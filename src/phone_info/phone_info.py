"""
        ██▄██ ▄▀▄ █▀▄ █▀▀ . █▀▄ █░█
        █░▀░█ █▄█ █░█ █▀▀ . █▀▄ ▀█▀
        ▀░░░▀ ▀░▀ ▀▀░ ▀▀▀ . ▀▀░ ░▀░
▒▐█▀█─░▄█▀▄─▒▐▌▒▐▌░▐█▀▀▒██░░░░▐█▀█▄─░▄█▀▄─▒█▀█▀█
▒▐█▄█░▐█▄▄▐█░▒█▒█░░▐█▀▀▒██░░░░▐█▌▐█░▐█▄▄▐█░░▒█░░
▒▐█░░░▐█─░▐█░▒▀▄▀░░▐█▄▄▒██▄▄█░▐█▄█▀░▐█─░▐█░▒▄█▄░
"""

import sys
import logging
from pathlib import Path

import folium
import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

sys.path.insert(
    0,
    'src'
)

from logger.logger import Logger


class PhoneInfo:
    """
    Gets info by phone number.
    """

    def __init__(self,
                 number: str,
                 debug: bool = False) -> None:
        """
        Constructor.

        Args:
            * number - Phone number
            * debug - Activate debug mode
        """

        self.__number = number
        self.__logger = Logger(self.__class__.__name__)
        if debug:
            self.__logger.setLevel(logging.DEBUG)

    @property
    def number(self) -> str:
        """
        Property number method.
        """
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    def get_country(self) -> str:
        """
        Gets country by phone number.

        Returns:
            * Country
        """

        number = phonenumbers.parse(self.__number)
        self.__logger.info('Find country')
        country = geocoder.description_for_number(number, 'en')
        self.__logger.debug(f'Country found: {country}')
        return country

    def get_operator(self) -> str:
        """
        Gets operator by phone number.

        Returns:
            * Operator
        """

        number = phonenumbers.parse(self.__number)
        self.__logger.info('Find operator')
        operator = carrier.name_for_number(number, 'en')
        self.__logger.debug(f'Operator found: {operator}')
        return operator

    def draw_map(self,
                 api_key: str = None,
                 path_to_save: [str, Path] = None) -> None:
        """
        Draws map with phone location.
        If api_key is not given - map will not be drawn.

        Args:
            * api_key - If you want to get an approximate location,
                        then you need to get api_key from
                            https://opencagedata.com/
            * path_to_save - Path to save the map
        """

        if api_key is None:
            self.__logger.raise_fatal(ValueError('Api key not given'))

        geocode = OpenCageGeocode(api_key)
        location = self.get_country()
        results = geocode.geocode(location)

        self.__logger.info('Get lat and lng')
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        self.__logger.debug(f'Lat: {lat}, Lng: {lng}')

        my_map = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=location).add_to(my_map)

        self.__logger.info('Draw map')
        if path_to_save is None:
            my_map.save(f'{self.__number}.html')
            self.__logger.debug(f'Map was saved to {self.__number}.html')
        else:
            Path(path_to_save).mkdir(exist_ok=True, parents=True)
            my_map.save(f'{path_to_save}/{self.__number}.html')
            self.__logger.debug(f'Map was saved to '
                                f'{path_to_save}/{self.__number}.html')
