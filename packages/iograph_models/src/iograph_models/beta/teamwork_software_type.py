from __future__ import annotations
from enum import StrEnum


class TeamworkSoftwareType(StrEnum):
	adminAgent = "adminAgent"
	operatingSystem = "operatingSystem"
	teamsClient = "teamsClient"
	firmware = "firmware"
	partnerAgent = "partnerAgent"
	companyPortal = "companyPortal"
	unknownFutureValue = "unknownFutureValue"

