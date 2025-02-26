from __future__ import annotations
from enum import Enum


class CallRecordsProductFamily(Enum):
	unknown = "unknown"
	teams = "teams"
	skypeForBusiness = "skypeForBusiness"
	lync = "lync"
	unknownFutureValue = "unknownFutureValue"
	azureCommunicationServices = "azureCommunicationServices"

