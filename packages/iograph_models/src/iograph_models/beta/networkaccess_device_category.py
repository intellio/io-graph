from __future__ import annotations
from enum import StrEnum


class NetworkaccessDeviceCategory(StrEnum):
	client = "client"
	branch = "branch"
	unknownFutureValue = "unknownFutureValue"
	remoteNetwork = "remoteNetwork"

