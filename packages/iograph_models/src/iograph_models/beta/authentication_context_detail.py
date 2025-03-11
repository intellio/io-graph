from __future__ import annotations
from enum import StrEnum


class AuthenticationContextDetail(StrEnum):
	required = "required"
	previouslySatisfied = "previouslySatisfied"
	notApplicable = "notApplicable"
	unknownFutureValue = "unknownFutureValue"

