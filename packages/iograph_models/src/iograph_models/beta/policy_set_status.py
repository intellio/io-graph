from __future__ import annotations
from enum import StrEnum


class PolicySetStatus(StrEnum):
	unknown = "unknown"
	validating = "validating"
	partialSuccess = "partialSuccess"
	success = "success"
	error = "error"
	notAssigned = "notAssigned"

