from __future__ import annotations
from enum import StrEnum


class CloudPcUserAccessLevel(StrEnum):
	unrestricted = "unrestricted"
	restricted = "restricted"
	unknownFutureValue = "unknownFutureValue"

