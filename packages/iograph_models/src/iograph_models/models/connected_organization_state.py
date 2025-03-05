from __future__ import annotations
from enum import StrEnum


class ConnectedOrganizationState(StrEnum):
	configured = "configured"
	proposed = "proposed"
	unknownFutureValue = "unknownFutureValue"

