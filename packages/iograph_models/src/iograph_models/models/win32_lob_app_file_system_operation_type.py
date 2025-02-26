from __future__ import annotations
from enum import Enum


class Win32LobAppFileSystemOperationType(Enum):
	notConfigured = "notConfigured"
	exists = "exists"
	modifiedDate = "modifiedDate"
	createdDate = "createdDate"
	version = "version"
	sizeInMB = "sizeInMB"

