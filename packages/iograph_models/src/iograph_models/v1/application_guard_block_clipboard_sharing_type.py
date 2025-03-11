from __future__ import annotations
from enum import StrEnum


class ApplicationGuardBlockClipboardSharingType(StrEnum):
	notConfigured = "notConfigured"
	blockBoth = "blockBoth"
	blockHostToContainer = "blockHostToContainer"
	blockContainerToHost = "blockContainerToHost"
	blockNone = "blockNone"

