from __future__ import annotations
from enum import StrEnum


class OnlineMeetingProviderType(StrEnum):
	unknown = "unknown"
	skypeForBusiness = "skypeForBusiness"
	skypeForConsumer = "skypeForConsumer"
	teamsForBusiness = "teamsForBusiness"

