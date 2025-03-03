from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Trending(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	resourceReference: Optional[ResourceReference] = Field(default=None,alias="resourceReference",)
	resourceVisualization: Optional[ResourceVisualization] = Field(default=None,alias="resourceVisualization",)
	weight: float | str | ReferenceNumeric
	resource: Optional[Entity] = Field(default=None,alias="resource",)

from .resource_reference import ResourceReference
from .resource_visualization import ResourceVisualization
from .reference_numeric import ReferenceNumeric
from .entity import Entity

