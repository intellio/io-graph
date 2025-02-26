from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ObjectDefinition(BaseModel):
	attributes: list[AttributeDefinition] = Field(alias="attributes",)
	metadata: list[ObjectDefinitionMetadataEntry] = Field(alias="metadata",)
	name: Optional[str] = Field(default=None,alias="name",)
	supportedApis: list[Optional[str]] = Field(alias="supportedApis",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .attribute_definition import AttributeDefinition
from .object_definition_metadata_entry import ObjectDefinitionMetadataEntry

