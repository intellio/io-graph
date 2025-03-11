from __future__ import annotations
from enum import StrEnum


class SensitivityLabelTarget(StrEnum):
	email = "email"
	site = "site"
	unifiedGroup = "unifiedGroup"
	teamwork = "teamwork"
	unknownFutureValue = "unknownFutureValue"

