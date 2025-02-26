from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SharedInsight(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	lastShared: Optional[SharingDetail] = Field(default=None,alias="lastShared",)
	resourceReference: Optional[ResourceReference] = Field(default=None,alias="resourceReference",)
	resourceVisualization: Optional[ResourceVisualization] = Field(default=None,alias="resourceVisualization",)
	sharingHistory: list[SharingDetail] = Field(alias="sharingHistory",)
	lastSharedMethod: Optional[Entity] = Field(default=None,alias="lastSharedMethod",)
	resource: Optional[Entity] = Field(default=None,alias="resource",)

from .sharing_detail import SharingDetail
from .resource_reference import ResourceReference
from .resource_visualization import ResourceVisualization
from .sharing_detail import SharingDetail
from .entity import Entity
from .entity import Entity

