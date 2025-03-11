from __future__ import annotations
from enum import StrEnum


class SecurityDisableUserEntityIdentifier(StrEnum):
	accountSid = "accountSid"
	initiatingProcessAccountSid = "initiatingProcessAccountSid"
	requestAccountSid = "requestAccountSid"
	onPremSid = "onPremSid"
	unknownFutureValue = "unknownFutureValue"

