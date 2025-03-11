from __future__ import annotations
from enum import StrEnum


class PowerActionType(StrEnum):
	notConfigured = "notConfigured"
	noAction = "noAction"
	sleep = "sleep"
	hibernate = "hibernate"
	shutdown = "shutdown"

