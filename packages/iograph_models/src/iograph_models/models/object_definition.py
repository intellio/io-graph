from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ObjectDefinition(BaseModel):
	attributes: Optional[list[AttributeDefinition]] = Field(default=None,alias="attributes",)
	metadata: Optional[list[ObjectDefinitionMetadataEntry]] = Field(default=None,alias="metadata",)
	name: Optional[str] = Field(default=None,alias="name",)
	supportedApis: Optional[list[str]] = Field(default=None,alias="supportedApis",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .attribute_definition import AttributeDefinition
from .object_definition_metadata_entry import ObjectDefinitionMetadataEntry

