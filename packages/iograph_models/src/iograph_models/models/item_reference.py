from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ItemReference(BaseModel):
	driveId: Optional[str] = Field(default=None,alias="driveId",)
	driveType: Optional[str] = Field(default=None,alias="driveType",)
	id: Optional[str] = Field(default=None,alias="id",)
	name: Optional[str] = Field(default=None,alias="name",)
	path: Optional[str] = Field(default=None,alias="path",)
	shareId: Optional[str] = Field(default=None,alias="shareId",)
	sharepointIds: Optional[SharepointIds] = Field(default=None,alias="sharepointIds",)
	siteId: Optional[str] = Field(default=None,alias="siteId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .sharepoint_ids import SharepointIds

