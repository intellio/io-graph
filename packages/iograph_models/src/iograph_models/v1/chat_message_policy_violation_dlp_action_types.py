from __future__ import annotations
from enum import StrEnum


class ChatMessagePolicyViolationDlpActionTypes(StrEnum):
	none = "none"
	notifySender = "notifySender"
	blockAccess = "blockAccess"
	blockAccessExternal = "blockAccessExternal"

