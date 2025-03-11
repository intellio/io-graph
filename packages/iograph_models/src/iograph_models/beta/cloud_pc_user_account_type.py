from __future__ import annotations
from enum import StrEnum


class CloudPcUserAccountType(StrEnum):
	standardUser = "standardUser"
	administrator = "administrator"
	unknownFutureValue = "unknownFutureValue"

