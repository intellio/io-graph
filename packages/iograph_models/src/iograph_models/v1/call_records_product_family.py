from __future__ import annotations
from enum import StrEnum


class CallRecordsProductFamily(StrEnum):
	unknown = "unknown"
	teams = "teams"
	skypeForBusiness = "skypeForBusiness"
	lync = "lync"
	unknownFutureValue = "unknownFutureValue"
	azureCommunicationServices = "azureCommunicationServices"

