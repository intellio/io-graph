from __future__ import annotations
from enum import Enum


class AttestationLevel(Enum):
	attested = "attested"
	notAttested = "notAttested"
	unknownFutureValue = "unknownFutureValue"

