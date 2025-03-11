from __future__ import annotations
from enum import StrEnum


class EmbeddedSIMDeviceStateValue(StrEnum):
	notEvaluated = "notEvaluated"
	failed = "failed"
	installing = "installing"
	installed = "installed"
	deleting = "deleting"
	error = "error"
	deleted = "deleted"
	removedByUser = "removedByUser"

