from __future__ import annotations
from enum import StrEnum


class SecurityDeliveryLocation(StrEnum):
	unknown = "unknown"
	inbox_folder = "inbox_folder"
	junkFolder = "junkFolder"
	deletedFolder = "deletedFolder"
	quarantine = "quarantine"
	onprem_external = "onprem_external"
	failed = "failed"
	dropped = "dropped"
	others = "others"
	unknownFutureValue = "unknownFutureValue"

