from __future__ import annotations
from enum import Enum


class ConditionalAccessGrantControl(Enum):
	block = "block"
	mfa = "mfa"
	compliantDevice = "compliantDevice"
	domainJoinedDevice = "domainJoinedDevice"
	approvedApplication = "approvedApplication"
	compliantApplication = "compliantApplication"
	passwordChange = "passwordChange"
	unknownFutureValue = "unknownFutureValue"

