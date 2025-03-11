from __future__ import annotations
from enum import StrEnum


class VirtualEventStatus(StrEnum):
	draft = "draft"
	published = "published"
	canceled = "canceled"
	unknownFutureValue = "unknownFutureValue"

