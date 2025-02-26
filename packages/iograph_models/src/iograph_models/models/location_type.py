from __future__ import annotations
from enum import Enum


class LocationType(Enum):
	default = "default"
	conferenceRoom = "conferenceRoom"
	homeAddress = "homeAddress"
	businessAddress = "businessAddress"
	geoCoordinates = "geoCoordinates"
	streetAddress = "streetAddress"
	hotel = "hotel"
	restaurant = "restaurant"
	localBusiness = "localBusiness"
	postalAddress = "postalAddress"

