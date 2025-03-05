from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Trending(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	resourceReference: Optional[ResourceReference] = Field(alias="resourceReference",default=None,)
	resourceVisualization: Optional[ResourceVisualization] = Field(alias="resourceVisualization",default=None,)
	weight: float | str | ReferenceNumeric
	resource: SerializeAsAny[Optional[Entity]] = Field(alias="resource",default=None,)

from .resource_reference import ResourceReference
from .resource_visualization import ResourceVisualization
from .reference_numeric import ReferenceNumeric
from .entity import Entity

