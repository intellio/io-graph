from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SynchronizationRule(BaseModel):
	containerFilter: Optional[ContainerFilter] = Field(alias="containerFilter",default=None,)
	editable: Optional[bool] = Field(alias="editable",default=None,)
	groupFilter: Optional[GroupFilter] = Field(alias="groupFilter",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	metadata: Optional[list[StringKeyStringValuePair]] = Field(alias="metadata",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	objectMappings: Optional[list[ObjectMapping]] = Field(alias="objectMappings",default=None,)
	priority: Optional[int] = Field(alias="priority",default=None,)
	sourceDirectoryName: Optional[str] = Field(alias="sourceDirectoryName",default=None,)
	targetDirectoryName: Optional[str] = Field(alias="targetDirectoryName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .container_filter import ContainerFilter
from .group_filter import GroupFilter
from .string_key_string_value_pair import StringKeyStringValuePair
from .object_mapping import ObjectMapping

