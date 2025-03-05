from __future__ import annotations
from enum import StrEnum


class ApplicationGuardBlockFileTransferType(StrEnum):
	notConfigured = "notConfigured"
	blockImageAndTextFile = "blockImageAndTextFile"
	blockImageFile = "blockImageFile"
	blockNone = "blockNone"
	blockTextFile = "blockTextFile"

