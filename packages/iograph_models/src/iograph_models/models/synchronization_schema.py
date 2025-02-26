from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SynchronizationSchema(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	synchronizationRules: list[SynchronizationRule] = Field(alias="synchronizationRules",)
	version: Optional[str] = Field(default=None,alias="version",)
	directories: list[DirectoryDefinition] = Field(alias="directories",)

from .synchronization_rule import SynchronizationRule
from .directory_definition import DirectoryDefinition

