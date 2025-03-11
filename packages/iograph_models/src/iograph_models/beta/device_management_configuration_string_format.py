from __future__ import annotations
from enum import StrEnum


class DeviceManagementConfigurationStringFormat(StrEnum):
	none = "none"
	email = "email"
	guid = "guid"
	ip = "ip"
	base64 = "base64"
	url = "url"
	version = "version"
	xml = "xml"
	date = "date"
	time = "time"
	binary = "binary"
	regEx = "regEx"
	json = "json"
	dateTime = "dateTime"
	surfaceHub = "surfaceHub"
	bashScript = "bashScript"
	unknownFutureValue = "unknownFutureValue"

