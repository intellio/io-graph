from __future__ import annotations
from enum import StrEnum


class ComplianceStatus(StrEnum):
	unknown = "unknown"
	notApplicable = "notApplicable"
	compliant = "compliant"
	remediated = "remediated"
	nonCompliant = "nonCompliant"
	error = "error"
	conflict = "conflict"
	notAssigned = "notAssigned"

