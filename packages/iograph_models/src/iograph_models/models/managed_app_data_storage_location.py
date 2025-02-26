from __future__ import annotations
from enum import Enum


class ManagedAppDataStorageLocation(Enum):
	oneDriveForBusiness = "oneDriveForBusiness"
	sharePoint = "sharePoint"
	box = "box"
	localStorage = "localStorage"

