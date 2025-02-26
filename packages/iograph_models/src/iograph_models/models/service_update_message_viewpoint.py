from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ServiceUpdateMessageViewpoint(BaseModel):
	isArchived: Optional[bool] = Field(default=None,alias="isArchived",)
	isFavorited: Optional[bool] = Field(default=None,alias="isFavorited",)
	isRead: Optional[bool] = Field(default=None,alias="isRead",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


