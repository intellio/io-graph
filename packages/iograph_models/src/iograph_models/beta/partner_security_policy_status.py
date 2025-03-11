from __future__ import annotations
from enum import StrEnum


class PartnerSecurityPolicyStatus(StrEnum):
	enabled = "enabled"
	disabled = "disabled"
	unknownFutureValue = "unknownFutureValue"

