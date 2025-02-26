from __future__ import annotations
from enum import Enum


class ApplicationGuardBlockFileTransferType(Enum):
	notConfigured = "notConfigured"
	blockImageAndTextFile = "blockImageAndTextFile"
	blockImageFile = "blockImageFile"
	blockNone = "blockNone"
	blockTextFile = "blockTextFile"

