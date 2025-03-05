from __future__ import annotations
from enum import StrEnum


class Win32LobAppFileSystemOperationType(StrEnum):
	notConfigured = "notConfigured"
	exists = "exists"
	modifiedDate = "modifiedDate"
	createdDate = "createdDate"
	version = "version"
	sizeInMB = "sizeInMB"

