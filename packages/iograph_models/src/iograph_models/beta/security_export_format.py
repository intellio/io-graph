from __future__ import annotations
from enum import StrEnum


class SecurityExportFormat(StrEnum):
	pst = "pst"
	msg = "msg"
	eml = "eml"
	unknownFutureValue = "unknownFutureValue"

