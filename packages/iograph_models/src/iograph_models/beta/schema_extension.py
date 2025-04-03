from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SchemaExtension(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.schemaExtension"] = Field(alias="@odata.type", default="#microsoft.graph.schemaExtension")
	description: Optional[str] = Field(alias="description", default=None,)
	owner: Optional[str] = Field(alias="owner", default=None,)
	properties: Optional[list[ExtensionSchemaProperty]] = Field(alias="properties", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	targetTypes: Optional[list[str]] = Field(alias="targetTypes", default=None,)

from .extension_schema_property import ExtensionSchemaProperty
