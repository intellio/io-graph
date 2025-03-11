from __future__ import annotations
from enum import StrEnum


class AttestationLevel(StrEnum):
	attested = "attested"
	notAttested = "notAttested"
	unknownFutureValue = "unknownFutureValue"

