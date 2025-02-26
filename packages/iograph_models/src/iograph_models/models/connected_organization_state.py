from __future__ import annotations
from enum import Enum


class ConnectedOrganizationState(Enum):
	configured = "configured"
	proposed = "proposed"
	unknownFutureValue = "unknownFutureValue"

