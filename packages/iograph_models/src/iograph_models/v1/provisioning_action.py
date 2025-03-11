from __future__ import annotations
from enum import StrEnum


class ProvisioningAction(StrEnum):
	other = "other"
	create = "create"
	delete = "delete"
	disable = "disable"
	update = "update"
	stagedDelete = "stagedDelete"
	unknownFutureValue = "unknownFutureValue"

