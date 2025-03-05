from __future__ import annotations
from enum import StrEnum


class VirtualEventRegistrationPredefinedQuestionLabel(StrEnum):
	street = "street"
	city = "city"
	state = "state"
	postalCode = "postalCode"
	countryOrRegion = "countryOrRegion"
	industry = "industry"
	jobTitle = "jobTitle"
	organization = "organization"
	unknownFutureValue = "unknownFutureValue"

