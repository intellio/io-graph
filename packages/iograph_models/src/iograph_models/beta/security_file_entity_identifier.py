from __future__ import annotations
from enum import StrEnum


class SecurityFileEntityIdentifier(StrEnum):
	sha1 = "sha1"
	initiatingProcessSHA1 = "initiatingProcessSHA1"
	sha256 = "sha256"
	initiatingProcessSHA256 = "initiatingProcessSHA256"
	unknownFutureValue = "unknownFutureValue"

