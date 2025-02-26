from __future__ import annotations
from enum import Enum


class OnlineMeetingProviderType(Enum):
	unknown = "unknown"
	skypeForBusiness = "skypeForBusiness"
	skypeForConsumer = "skypeForConsumer"
	teamsForBusiness = "teamsForBusiness"

