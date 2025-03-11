from __future__ import annotations
from enum import StrEnum


class AndroidDeviceOwnerPlayStoreMode(StrEnum):
	notConfigured = "notConfigured"
	allowList = "allowList"
	blockList = "blockList"

