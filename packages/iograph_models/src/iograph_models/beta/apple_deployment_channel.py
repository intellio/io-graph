from __future__ import annotations
from enum import StrEnum


class AppleDeploymentChannel(StrEnum):
	deviceChannel = "deviceChannel"
	userChannel = "userChannel"
	unknownFutureValue = "unknownFutureValue"

