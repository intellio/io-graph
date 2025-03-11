from __future__ import annotations
from enum import StrEnum


class DelegateMeetingMessageDeliveryOptions(StrEnum):
	sendToDelegateAndInformationToPrincipal = "sendToDelegateAndInformationToPrincipal"
	sendToDelegateAndPrincipal = "sendToDelegateAndPrincipal"
	sendToDelegateOnly = "sendToDelegateOnly"

