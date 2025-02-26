from __future__ import annotations
from enum import Enum


class VirtualEventStatus(Enum):
	draft = "draft"
	published = "published"
	canceled = "canceled"
	unknownFutureValue = "unknownFutureValue"

