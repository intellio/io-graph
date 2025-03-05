from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UsedInsight(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	lastUsed: Optional[UsageDetails] = Field(default=None,alias="lastUsed",)
	resourceReference: Optional[ResourceReference] = Field(default=None,alias="resourceReference",)
	resourceVisualization: Optional[ResourceVisualization] = Field(default=None,alias="resourceVisualization",)
	resource: SerializeAsAny[Optional[Entity]] = Field(default=None,alias="resource",)

from .usage_details import UsageDetails
from .resource_reference import ResourceReference
from .resource_visualization import ResourceVisualization
from .entity import Entity

