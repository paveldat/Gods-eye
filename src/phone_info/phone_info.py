"""
        ██▄██ ▄▀▄ █▀▄ █▀▀ . █▀▄ █░█
        █░▀░█ █▄█ █░█ █▀▀ . █▀▄ ▀█▀
        ▀░░░▀ ▀░▀ ▀▀░ ▀▀▀ . ▀▀░ ░▀░
▒▐█▀█─░▄█▀▄─▒▐▌▒▐▌░▐█▀▀▒██░░░░▐█▀█▄─░▄█▀▄─▒█▀█▀█
▒▐█▄█░▐█▄▄▐█░▒█▒█░░▐█▀▀▒██░░░░▐█▌▐█░▐█▄▄▐█░░▒█░░
▒▐█░░░▐█─░▐█░▒▀▄▀░░▐█▄▄▒██▄▄█░▐█▄█▀░▐█─░▐█░▒▄█▄░
"""

import logging
import sys
from pathlib import Path

import folium
import phonenumbers
import requests
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier, geocoder

sys.path.insert(0, "src")

from logger.logger import Logger


class PhoneInfo:
    """
    Gets info by phone number.
    """

    def __init__(self, number: str, debug: bool = False) -> None:
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
        self.__logger.info("Find country")
        country = geocoder.description_for_number(number, "en")
        self.__logger.debug(f"Country found: {country}")
        return country

    def get_operator(self) -> str:
        """
        Gets operator by phone number.

        Returns:
            * Operator
        """

        number = phonenumbers.parse(self.__number)
        self.__logger.info("Find operator")
        operator = carrier.name_for_number(number, "en")
        self.__logger.debug(f"Operator found: {operator}")
        return operator

    def draw_map(self, api_key: str = None, path_to_save: [str, Path] = None) -> None:
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
            self.__logger.raise_fatal(ValueError("Api key not given"))

        geocode = OpenCageGeocode(api_key)
        location = self.get_country()
        results = geocode.geocode(location)

        self.__logger.info("Get lat and lng")
        lat = results[0]["geometry"]["lat"]
        lng = results[0]["geometry"]["lng"]
        self.__logger.debug(f"Lat: {lat}, Lng: {lng}")

        my_map = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=location).add_to(my_map)

        self.__logger.info("Draw map")
        if path_to_save is None:
            my_map.save(f"{self.__number}.html")
            self.__logger.debug(f"Map was saved to {self.__number}.html")
        else:
            Path(path_to_save).mkdir(exist_ok=True, parents=True)
            my_map.save(f"{path_to_save}/{self.__number}.html")
            self.__logger.debug(
                f"Map was saved to " f"{path_to_save}/{self.__number}.html"
            )


class ProbivApiPhoneInfo:
    """
    Gets info by phone number.
    First of all, you need to register and get a subscription to this api:
    https://probivapi.com/.
    """

    def __init__(self, secret_key: str, number: str, debug: bool = False) -> None:
        """
        Constructor.

        Args:
            * secret_key - Secret key from https://probivapi.com/
            * number - Phone number
            * debug - Activate debug mode
        """

        self.__secret_key = secret_key
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

    def get_info_by_number(self) -> None:
        """
        Gets all found info by phone number.
        """

        url = f"https://probivapi.com/api/phone/info/{self.__number}"

        head = {"X-Auth": self.__secret_key}

        response = requests.get(url, headers=head)
        self.__logger.debug(response.text)

        try:
            json_response = response.json()
        except Exception:
            json_response = {}

        callapp_data = json_response.get("callapp", {})
        callapp_api_name = callapp_data.get("name", "Not found")
        callapp_emails = ", ".join(
            [email.get("email") for email in callapp_data.get("emails", [])]
        )
        callapp_websites = ", ".join(
            [site.get("websiteUrl") for site in callapp_data.get("websites", [])]
        )
        callapp_addresses = ", ".join(
            [addr.get("street") for addr in callapp_data.get("addresses", [])]
        )
        callapp_description = callapp_data.get("description", "Not found")
        callapp_opening_hours = ", ".join(
            [
                f"{day}: {', '.join(hours)}"
                for day, hours in callapp_data.get("openingHours", {}).items()
            ]
        )
        callapp_lat = callapp_data.get("lat", "Not found")
        callapp_lng = callapp_data.get("lng", "Not found")
        callapp_spam_score = callapp_data.get("spamScore", "Not found")
        callapp_priority = callapp_data.get("priority", "Not found")
        eyecon_api_name = json_response.get("eyecon", "Not found")
        viewcaller_name_list = [
            tag.get("name", "Not found") for tag in json_response.get("viewcaller", [])
        ]
        viewcaller_api_name = ", ".join(viewcaller_name_list)

        info = f"""\n✅ Info for {self.__number}
┣ 📱 ФИО (CallApp): {callapp_api_name}
┣ 📧 Emails (CallApp): {callapp_emails}
┣ 🌐 Сайты (CallApp): {callapp_websites}
┣ 🏠 Адреса (CallApp): {callapp_addresses}
┣ 📝 Описание (CallApp): {callapp_description}
┣ 🕒 Часы работы (CallApp): {callapp_opening_hours}
┣ 🌍 Координаты (CallApp): {callapp_lat}, {callapp_lng}
┣ ⚠️ Spam Score (CallApp): {callapp_spam_score}
┣ ⭐ Priority (CallApp): {callapp_priority}
┣ 🌐 ФИО (EyeCon): {eyecon_api_name}
┣ 🔎 ФИО (ViewCaller): {viewcaller_api_name}"""

        self.__logger.info(info)
