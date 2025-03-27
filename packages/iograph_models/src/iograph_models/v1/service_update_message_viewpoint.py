from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceUpdateMessageViewpoint(BaseModel):
	isArchived: Optional[bool] = Field(alias="isArchived", default=None,)
	isFavorited: Optional[bool] = Field(alias="isFavorited", default=None,)
	isRead: Optional[bool] = Field(alias="isRead", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


