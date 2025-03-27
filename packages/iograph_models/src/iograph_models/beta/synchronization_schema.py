from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationSchema(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	synchronizationRules: Optional[list[SynchronizationRule]] = Field(alias="synchronizationRules", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	directories: Optional[list[DirectoryDefinition]] = Field(alias="directories", default=None,)

from .synchronization_rule import SynchronizationRule
from .directory_definition import DirectoryDefinition

