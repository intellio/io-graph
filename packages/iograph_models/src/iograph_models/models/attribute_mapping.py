from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AttributeMapping(BaseModel):
	defaultValue: Optional[str] = Field(default=None,alias="defaultValue",)
	exportMissingReferences: Optional[bool] = Field(default=None,alias="exportMissingReferences",)
	flowBehavior: Optional[AttributeFlowBehavior] = Field(default=None,alias="flowBehavior",)
	flowType: Optional[AttributeFlowType] = Field(default=None,alias="flowType",)
	matchingPriority: Optional[int] = Field(default=None,alias="matchingPriority",)
	source: Optional[AttributeMappingSource] = Field(default=None,alias="source",)
	targetAttributeName: Optional[str] = Field(default=None,alias="targetAttributeName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .attribute_flow_behavior import AttributeFlowBehavior
from .attribute_flow_type import AttributeFlowType
from .attribute_mapping_source import AttributeMappingSource

