from __future__ import annotations
from enum import Enum


class ApplicationGuardBlockClipboardSharingType(Enum):
	notConfigured = "notConfigured"
	blockBoth = "blockBoth"
	blockHostToContainer = "blockHostToContainer"
	blockContainerToHost = "blockContainerToHost"
	blockNone = "blockNone"

