from __future__ import annotations
from enum import StrEnum


class UserAction(StrEnum):
	registerSecurityInformation = "registerSecurityInformation"
	registerOrJoinDevices = "registerOrJoinDevices"
	unknownFutureValue = "unknownFutureValue"

