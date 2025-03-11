from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ItemAttachment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	contentType: Optional[str] = Field(alias="contentType",default=None,)
	isInline: Optional[bool] = Field(alias="isInline",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	size: Optional[int] = Field(alias="size",default=None,)
	item: SerializeAsAny[Optional[OutlookItem]] = Field(alias="item",default=None,)

from .outlook_item import OutlookItem

