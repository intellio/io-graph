from __future__ import annotations
from enum import StrEnum


class FolderProtectionType(StrEnum):
	userDefined = "userDefined"
	enable = "enable"
	auditMode = "auditMode"
	blockDiskModification = "blockDiskModification"
	auditDiskModification = "auditDiskModification"

