from __future__ import annotations
from enum import Enum


class ProvisioningAction(Enum):
	other = "other"
	create = "create"
	delete = "delete"
	disable = "disable"
	update = "update"
	stagedDelete = "stagedDelete"
	unknownFutureValue = "unknownFutureValue"

