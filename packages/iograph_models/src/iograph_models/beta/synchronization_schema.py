from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SynchronizationSchema(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.synchronizationSchema"] = Field(alias="@odata.type",)
	synchronizationRules: Optional[list[SynchronizationRule]] = Field(alias="synchronizationRules", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	directories: Optional[list[DirectoryDefinition]] = Field(alias="directories", default=None,)

from .synchronization_rule import SynchronizationRule
from .directory_definition import DirectoryDefinition
