from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DirectoryDefinition(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	discoverabilities: Optional[DirectoryDefinitionDiscoverabilities] = Field(default=None,alias="discoverabilities",)
	discoveryDateTime: Optional[datetime] = Field(default=None,alias="discoveryDateTime",)
	name: Optional[str] = Field(default=None,alias="name",)
	objects: list[ObjectDefinition] = Field(alias="objects",)
	readOnly: Optional[bool] = Field(default=None,alias="readOnly",)
	version: Optional[str] = Field(default=None,alias="version",)

from .directory_definition_discoverabilities import DirectoryDefinitionDiscoverabilities
from .object_definition import ObjectDefinition

