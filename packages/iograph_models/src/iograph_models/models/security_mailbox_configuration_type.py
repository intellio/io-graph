from __future__ import annotations
from enum import StrEnum


class SecurityMailboxConfigurationType(StrEnum):
	mailForwardingRule = "mailForwardingRule"
	owaSettings = "owaSettings"
	ewsSettings = "ewsSettings"
	mailDelegation = "mailDelegation"
	userInboxRule = "userInboxRule"
	unknownFutureValue = "unknownFutureValue"

