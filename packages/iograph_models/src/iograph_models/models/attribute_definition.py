from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AttributeDefinition(BaseModel):
	anchor: Optional[bool] = Field(default=None,alias="anchor",)
	apiExpressions: list[StringKeyStringValuePair] = Field(alias="apiExpressions",)
	caseExact: Optional[bool] = Field(default=None,alias="caseExact",)
	defaultValue: Optional[str] = Field(default=None,alias="defaultValue",)
	flowNullValues: Optional[bool] = Field(default=None,alias="flowNullValues",)
	metadata: list[AttributeDefinitionMetadataEntry] = Field(alias="metadata",)
	multivalued: Optional[bool] = Field(default=None,alias="multivalued",)
	mutability: Optional[Mutability] = Field(default=None,alias="mutability",)
	name: Optional[str] = Field(default=None,alias="name",)
	referencedObjects: list[ReferencedObject] = Field(alias="referencedObjects",)
	required: Optional[bool] = Field(default=None,alias="required",)
	type: Optional[AttributeType] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .string_key_string_value_pair import StringKeyStringValuePair
from .attribute_definition_metadata_entry import AttributeDefinitionMetadataEntry
from .mutability import Mutability
from .referenced_object import ReferencedObject
from .attribute_type import AttributeType

