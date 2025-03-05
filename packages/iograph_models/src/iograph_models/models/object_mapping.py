from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ObjectMapping(BaseModel):
	attributeMappings: Optional[list[AttributeMapping]] = Field(alias="attributeMappings",default=None,)
	enabled: Optional[bool] = Field(alias="enabled",default=None,)
	flowTypes: Optional[str | ObjectFlowTypes] = Field(alias="flowTypes",default=None,)
	metadata: Optional[list[ObjectMappingMetadataEntry]] = Field(alias="metadata",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	scope: Optional[Filter] = Field(alias="scope",default=None,)
	sourceObjectName: Optional[str] = Field(alias="sourceObjectName",default=None,)
	targetObjectName: Optional[str] = Field(alias="targetObjectName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .attribute_mapping import AttributeMapping
from .object_flow_types import ObjectFlowTypes
from .object_mapping_metadata_entry import ObjectMappingMetadataEntry
from .filter import Filter

