from __future__ import annotations
from enum import Enum


class VirtualEventRegistrationPredefinedQuestionLabel(Enum):
	street = "street"
	city = "city"
	state = "state"
	postalCode = "postalCode"
	countryOrRegion = "countryOrRegion"
	industry = "industry"
	jobTitle = "jobTitle"
	organization = "organization"
	unknownFutureValue = "unknownFutureValue"

