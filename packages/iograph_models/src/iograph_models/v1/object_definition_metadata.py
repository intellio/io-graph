from __future__ import annotations
from enum import StrEnum


class ObjectDefinitionMetadata(StrEnum):
	PropertyNameAccountEnabled = "PropertyNameAccountEnabled"
	PropertyNameSoftDeleted = "PropertyNameSoftDeleted"
	IsSoftDeletionSupported = "IsSoftDeletionSupported"
	IsSynchronizeAllSupported = "IsSynchronizeAllSupported"
	ConnectorDataStorageRequired = "ConnectorDataStorageRequired"
	Extensions = "Extensions"
	BaseObjectName = "BaseObjectName"

