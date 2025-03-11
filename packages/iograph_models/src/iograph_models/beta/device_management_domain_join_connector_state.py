from __future__ import annotations
from enum import StrEnum


class DeviceManagementDomainJoinConnectorState(StrEnum):
	active = "active"
	error = "error"
	inactive = "inactive"

