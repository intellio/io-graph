from __future__ import annotations
from enum import StrEnum


class ManagedAppNotificationRestriction(StrEnum):
	allow = "allow"
	blockOrganizationalData = "blockOrganizationalData"
	block = "block"

