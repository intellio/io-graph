from __future__ import annotations
from enum import StrEnum


class AuthenticationAppAdminConfiguration(StrEnum):
	notApplicable = "notApplicable"
	enabled = "enabled"
	disabled = "disabled"
	unknownFutureValue = "unknownFutureValue"

