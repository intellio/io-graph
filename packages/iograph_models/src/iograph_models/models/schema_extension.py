from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SchemaExtension(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	owner: Optional[str] = Field(default=None,alias="owner",)
	properties: list[ExtensionSchemaProperty] = Field(alias="properties",)
	status: Optional[str] = Field(default=None,alias="status",)
	targetTypes: list[str] = Field(alias="targetTypes",)

from .extension_schema_property import ExtensionSchemaProperty

