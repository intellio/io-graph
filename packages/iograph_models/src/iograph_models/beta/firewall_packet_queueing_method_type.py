from __future__ import annotations
from enum import StrEnum


class FirewallPacketQueueingMethodType(StrEnum):
	deviceDefault = "deviceDefault"
	disabled = "disabled"
	queueInbound = "queueInbound"
	queueOutbound = "queueOutbound"
	queueBoth = "queueBoth"

