from __future__ import annotations
from enum import StrEnum


class PayloadIndustry(StrEnum):
	unknown = "unknown"
	other = "other"
	banking = "banking"
	businessServices = "businessServices"
	consumerServices = "consumerServices"
	education = "education"
	energy = "energy"
	construction = "construction"
	consulting = "consulting"
	financialServices = "financialServices"
	government = "government"
	hospitality = "hospitality"
	insurance = "insurance"
	legal = "legal"
	courierServices = "courierServices"
	IT = "IT"
	healthcare = "healthcare"
	manufacturing = "manufacturing"
	retail = "retail"
	telecom = "telecom"
	realEstate = "realEstate"
	unknownFutureValue = "unknownFutureValue"

