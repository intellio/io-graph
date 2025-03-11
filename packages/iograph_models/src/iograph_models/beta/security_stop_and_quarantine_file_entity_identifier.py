from __future__ import annotations
from enum import StrEnum


class SecurityStopAndQuarantineFileEntityIdentifier(StrEnum):
	deviceId = "deviceId"
	sha1 = "sha1"
	initiatingProcessSHA1 = "initiatingProcessSHA1"
	unknownFutureValue = "unknownFutureValue"

