from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AttributeMapping(BaseModel):
	defaultValue: Optional[str] = Field(alias="defaultValue",default=None,)
	exportMissingReferences: Optional[bool] = Field(alias="exportMissingReferences",default=None,)
	flowBehavior: Optional[AttributeFlowBehavior | str] = Field(alias="flowBehavior",default=None,)
	flowType: Optional[AttributeFlowType | str] = Field(alias="flowType",default=None,)
	matchingPriority: Optional[int] = Field(alias="matchingPriority",default=None,)
	source: Optional[AttributeMappingSource] = Field(alias="source",default=None,)
	targetAttributeName: Optional[str] = Field(alias="targetAttributeName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .attribute_flow_behavior import AttributeFlowBehavior
from .attribute_flow_type import AttributeFlowType
from .attribute_mapping_source import AttributeMappingSource

