from __future__ import annotations
from enum import Enum


class FirewallPacketQueueingMethodType(Enum):
	deviceDefault = "deviceDefault"
	disabled = "disabled"
	queueInbound = "queueInbound"
	queueOutbound = "queueOutbound"
	queueBoth = "queueBoth"

