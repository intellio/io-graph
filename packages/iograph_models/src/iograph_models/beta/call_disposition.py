from __future__ import annotations
from enum import StrEnum


class CallDisposition(StrEnum):
	default = "default"
	simultaneousRing = "simultaneousRing"
	forward = "forward"

