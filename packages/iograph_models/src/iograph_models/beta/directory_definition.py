from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DirectoryDefinition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	discoverabilities: Optional[DirectoryDefinitionDiscoverabilities | str] = Field(alias="discoverabilities",default=None,)
	discoveryDateTime: Optional[datetime] = Field(alias="discoveryDateTime",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	objects: Optional[list[ObjectDefinition]] = Field(alias="objects",default=None,)
	readOnly: Optional[bool] = Field(alias="readOnly",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)

from .directory_definition_discoverabilities import DirectoryDefinitionDiscoverabilities
from .object_definition import ObjectDefinition

