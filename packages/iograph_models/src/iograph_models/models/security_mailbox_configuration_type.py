from __future__ import annotations
from enum import Enum


class SecurityMailboxConfigurationType(Enum):
	mailForwardingRule = "mailForwardingRule"
	owaSettings = "owaSettings"
	ewsSettings = "ewsSettings"
	mailDelegation = "mailDelegation"
	userInboxRule = "userInboxRule"
	unknownFutureValue = "unknownFutureValue"

