from __future__ import annotations
from enum import Enum


class SecurityExportFormat(Enum):
	pst = "pst"
	msg = "msg"
	eml = "eml"
	unknownFutureValue = "unknownFutureValue"

