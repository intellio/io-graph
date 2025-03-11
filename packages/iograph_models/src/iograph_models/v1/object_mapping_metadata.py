from __future__ import annotations
from enum import StrEnum


class ObjectMappingMetadata(StrEnum):
	EscrowBehavior = "EscrowBehavior"
	DisableMonitoringForChanges = "DisableMonitoringForChanges"
	OriginalJoiningProperty = "OriginalJoiningProperty"
	Disposition = "Disposition"
	IsCustomerDefined = "IsCustomerDefined"
	ExcludeFromReporting = "ExcludeFromReporting"
	Unsynchronized = "Unsynchronized"

