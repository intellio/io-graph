from __future__ import annotations
from enum import Enum


class AgreementAcceptanceState(Enum):
	accepted = "accepted"
	declined = "declined"
	unknownFutureValue = "unknownFutureValue"

