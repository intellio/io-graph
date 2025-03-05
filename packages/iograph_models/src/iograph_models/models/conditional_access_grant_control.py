from __future__ import annotations
from enum import StrEnum


class ConditionalAccessGrantControl(StrEnum):
	block = "block"
	mfa = "mfa"
	compliantDevice = "compliantDevice"
	domainJoinedDevice = "domainJoinedDevice"
	approvedApplication = "approvedApplication"
	compliantApplication = "compliantApplication"
	passwordChange = "passwordChange"
	unknownFutureValue = "unknownFutureValue"

