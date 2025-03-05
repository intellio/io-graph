from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class FileAttachment(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	contentType: Optional[str] = Field(alias="contentType",default=None,)
	isInline: Optional[bool] = Field(alias="isInline",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	size: Optional[int] = Field(alias="size",default=None,)
	contentBytes: Optional[str] = Field(alias="contentBytes",default=None,)
	contentId: Optional[str] = Field(alias="contentId",default=None,)
	contentLocation: Optional[str] = Field(alias="contentLocation",default=None,)


