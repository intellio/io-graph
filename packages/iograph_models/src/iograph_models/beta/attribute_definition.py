from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AttributeDefinition(BaseModel):
	anchor: Optional[bool] = Field(alias="anchor", default=None,)
	apiExpressions: Optional[list[StringKeyStringValuePair]] = Field(alias="apiExpressions", default=None,)
	caseExact: Optional[bool] = Field(alias="caseExact", default=None,)
	defaultValue: Optional[str] = Field(alias="defaultValue", default=None,)
	flowNullValues: Optional[bool] = Field(alias="flowNullValues", default=None,)
	metadata: Optional[list[AttributeDefinitionMetadataEntry]] = Field(alias="metadata", default=None,)
	multivalued: Optional[bool] = Field(alias="multivalued", default=None,)
	mutability: Optional[Mutability | str] = Field(alias="mutability", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	referencedObjects: Optional[list[ReferencedObject]] = Field(alias="referencedObjects", default=None,)
	required: Optional[bool] = Field(alias="required", default=None,)
	type: Optional[AttributeType | str] = Field(alias="type", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .string_key_string_value_pair import StringKeyStringValuePair
from .attribute_definition_metadata_entry import AttributeDefinitionMetadataEntry
from .mutability import Mutability
from .referenced_object import ReferencedObject
from .attribute_type import AttributeType
