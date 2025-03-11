from __future__ import annotations
from enum import StrEnum


class SecurityForceUserPasswordResetEntityIdentifier(StrEnum):
	accountSid = "accountSid"
	initiatingProcessAccountSid = "initiatingProcessAccountSid"
	requestAccountSid = "requestAccountSid"
	onPremSid = "onPremSid"
	unknownFutureValue = "unknownFutureValue"

