from __future__ import annotations
from enum import StrEnum


class PartnerSecurityComplianceStatus(StrEnum):
	compliant = "compliant"
	noncomplaint = "noncomplaint"
	unknownFutureValue = "unknownFutureValue"

