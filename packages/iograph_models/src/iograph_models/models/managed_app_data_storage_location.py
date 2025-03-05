from __future__ import annotations
from enum import StrEnum


class ManagedAppDataStorageLocation(StrEnum):
	oneDriveForBusiness = "oneDriveForBusiness"
	sharePoint = "sharePoint"
	box = "box"
	localStorage = "localStorage"

