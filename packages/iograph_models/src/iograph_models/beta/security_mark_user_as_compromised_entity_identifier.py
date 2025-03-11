from __future__ import annotations
from enum import StrEnum


class SecurityMarkUserAsCompromisedEntityIdentifier(StrEnum):
	accountObjectId = "accountObjectId"
	initiatingProcessAccountObjectId = "initiatingProcessAccountObjectId"
	servicePrincipalId = "servicePrincipalId"
	recipientObjectId = "recipientObjectId"
	unknownFutureValue = "unknownFutureValue"

