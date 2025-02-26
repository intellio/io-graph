from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SynchronizationRule(BaseModel):
	containerFilter: Optional[ContainerFilter] = Field(default=None,alias="containerFilter",)
	editable: Optional[bool] = Field(default=None,alias="editable",)
	groupFilter: Optional[GroupFilter] = Field(default=None,alias="groupFilter",)
	id: Optional[str] = Field(default=None,alias="id",)
	metadata: list[StringKeyStringValuePair] = Field(alias="metadata",)
	name: Optional[str] = Field(default=None,alias="name",)
	objectMappings: list[ObjectMapping] = Field(alias="objectMappings",)
	priority: Optional[int] = Field(default=None,alias="priority",)
	sourceDirectoryName: Optional[str] = Field(default=None,alias="sourceDirectoryName",)
	targetDirectoryName: Optional[str] = Field(default=None,alias="targetDirectoryName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .container_filter import ContainerFilter
from .group_filter import GroupFilter
from .string_key_string_value_pair import StringKeyStringValuePair
from .object_mapping import ObjectMapping

