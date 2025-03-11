from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ObjectDefinition(BaseModel):
	attributes: Optional[list[AttributeDefinition]] = Field(alias="attributes",default=None,)
	metadata: Optional[list[ObjectDefinitionMetadataEntry]] = Field(alias="metadata",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	supportedApis: Optional[list[str]] = Field(alias="supportedApis",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .attribute_definition import AttributeDefinition
from .object_definition_metadata_entry import ObjectDefinitionMetadataEntry

