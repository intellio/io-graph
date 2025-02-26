from __future__ import annotations
from enum import Enum


class ComplianceStatus(Enum):
	unknown = "unknown"
	notApplicable = "notApplicable"
	compliant = "compliant"
	remediated = "remediated"
	nonCompliant = "nonCompliant"
	error = "error"
	conflict = "conflict"
	notAssigned = "notAssigned"

