from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SharedInsight(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	lastShared: Optional[SharingDetail] = Field(alias="lastShared",default=None,)
	resourceReference: Optional[ResourceReference] = Field(alias="resourceReference",default=None,)
	resourceVisualization: Optional[ResourceVisualization] = Field(alias="resourceVisualization",default=None,)
	sharingHistory: Optional[list[SharingDetail]] = Field(alias="sharingHistory",default=None,)
	lastSharedMethod: SerializeAsAny[Optional[Entity]] = Field(alias="lastSharedMethod",default=None,)
	resource: SerializeAsAny[Optional[Entity]] = Field(alias="resource",default=None,)

from .sharing_detail import SharingDetail
from .resource_reference import ResourceReference
from .resource_visualization import ResourceVisualization
from .sharing_detail import SharingDetail
from .entity import Entity
from .entity import Entity

