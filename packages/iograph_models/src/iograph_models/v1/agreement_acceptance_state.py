from __future__ import annotations
from enum import StrEnum


class AgreementAcceptanceState(StrEnum):
	accepted = "accepted"
	declined = "declined"
	unknownFutureValue = "unknownFutureValue"

