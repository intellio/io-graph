from __future__ import annotations
from enum import StrEnum


class AzureAttestationSettingStatus(StrEnum):
	notApplicable = "notApplicable"
	enabled = "enabled"
	disabled = "disabled"
	unknownFutureValue = "unknownFutureValue"

