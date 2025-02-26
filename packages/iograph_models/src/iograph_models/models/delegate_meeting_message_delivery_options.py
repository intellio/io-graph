from __future__ import annotations
from enum import Enum


class DelegateMeetingMessageDeliveryOptions(Enum):
	sendToDelegateAndInformationToPrincipal = "sendToDelegateAndInformationToPrincipal"
	sendToDelegateAndPrincipal = "sendToDelegateAndPrincipal"
	sendToDelegateOnly = "sendToDelegateOnly"

