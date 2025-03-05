from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SchemaExtension(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	owner: Optional[str] = Field(default=None,alias="owner",)
	properties: Optional[list[ExtensionSchemaProperty]] = Field(default=None,alias="properties",)
	status: Optional[str] = Field(default=None,alias="status",)
	targetTypes: Optional[list[str]] = Field(default=None,alias="targetTypes",)

from .extension_schema_property import ExtensionSchemaProperty

