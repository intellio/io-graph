from __future__ import annotations
from enum import Enum


class ChatMessagePolicyViolationDlpActionTypes(Enum):
	none = "none"
	notifySender = "notifySender"
	blockAccess = "blockAccess"
	blockAccessExternal = "blockAccessExternal"

