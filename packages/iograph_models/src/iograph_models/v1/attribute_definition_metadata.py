from __future__ import annotations
from enum import StrEnum


class AttributeDefinitionMetadata(StrEnum):
	BaseAttributeName = "BaseAttributeName"
	ComplexObjectDefinition = "ComplexObjectDefinition"
	IsContainer = "IsContainer"
	IsCustomerDefined = "IsCustomerDefined"
	IsDomainQualified = "IsDomainQualified"
	LinkPropertyNames = "LinkPropertyNames"
	LinkTypeName = "LinkTypeName"
	MaximumLength = "MaximumLength"
	ReferencedProperty = "ReferencedProperty"

