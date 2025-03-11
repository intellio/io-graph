from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UsedInsight(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	lastUsed: Optional[UsageDetails] = Field(alias="lastUsed",default=None,)
	resourceReference: Optional[ResourceReference] = Field(alias="resourceReference",default=None,)
	resourceVisualization: Optional[ResourceVisualization] = Field(alias="resourceVisualization",default=None,)
	resource: SerializeAsAny[Optional[Entity]] = Field(alias="resource",default=None,)

from .usage_details import UsageDetails
from .resource_reference import ResourceReference
from .resource_visualization import ResourceVisualization
from .entity import Entity

