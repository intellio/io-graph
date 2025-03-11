from __future__ import annotations
from enum import StrEnum


class Win32LobAppFileSystemDetectionType(StrEnum):
	notConfigured = "notConfigured"
	exists = "exists"
	modifiedDate = "modifiedDate"
	createdDate = "createdDate"
	version = "version"
	sizeInMB = "sizeInMB"
	doesNotExist = "doesNotExist"

