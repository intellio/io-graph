from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ItemReference(BaseModel):
	driveId: Optional[str] = Field(alias="driveId", default=None,)
	driveType: Optional[str] = Field(alias="driveType", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	path: Optional[str] = Field(alias="path", default=None,)
	shareId: Optional[str] = Field(alias="shareId", default=None,)
	sharepointIds: Optional[SharepointIds] = Field(alias="sharepointIds", default=None,)
	siteId: Optional[str] = Field(alias="siteId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .sharepoint_ids import SharepointIds
