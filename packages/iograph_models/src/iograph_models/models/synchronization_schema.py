from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationSchema(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	synchronizationRules: Optional[list[SynchronizationRule]] = Field(default=None,alias="synchronizationRules",)
	version: Optional[str] = Field(default=None,alias="version",)
	directories: Optional[list[DirectoryDefinition]] = Field(default=None,alias="directories",)

from .synchronization_rule import SynchronizationRule
from .directory_definition import DirectoryDefinition

