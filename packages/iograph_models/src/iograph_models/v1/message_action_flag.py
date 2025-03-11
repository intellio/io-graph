from __future__ import annotations
from enum import StrEnum


class MessageActionFlag(StrEnum):
	any = "any"
	call = "call"
	doNotForward = "doNotForward"
	followUp = "followUp"
	fyi = "fyi"
	forward = "forward"
	noResponseNecessary = "noResponseNecessary"
	read = "read"
	reply = "reply"
	replyToAll = "replyToAll"
	review = "review"

