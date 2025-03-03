from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ObjectMapping(BaseModel):
	attributeMappings: Optional[list[AttributeMapping]] = Field(default=None,alias="attributeMappings",)
	enabled: Optional[bool] = Field(default=None,alias="enabled",)
	flowTypes: Optional[ObjectFlowTypes] = Field(default=None,alias="flowTypes",)
	metadata: Optional[list[ObjectMappingMetadataEntry]] = Field(default=None,alias="metadata",)
	name: Optional[str] = Field(default=None,alias="name",)
	scope: Optional[Filter] = Field(default=None,alias="scope",)
	sourceObjectName: Optional[str] = Field(default=None,alias="sourceObjectName",)
	targetObjectName: Optional[str] = Field(default=None,alias="targetObjectName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .attribute_mapping import AttributeMapping
from .object_flow_types import ObjectFlowTypes
from .object_mapping_metadata_entry import ObjectMappingMetadataEntry
from .filter import Filter

