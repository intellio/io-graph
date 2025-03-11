from __future__ import annotations
from enum import StrEnum


class PrivilegeManagementEndUserType(StrEnum):
	undetermined = "undetermined"
	azureAd = "azureAd"
	hybrid = "hybrid"
	local = "local"
	unknownFutureValue = "unknownFutureValue"

