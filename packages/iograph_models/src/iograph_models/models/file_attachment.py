from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class FileAttachment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	contentType: Optional[str] = Field(default=None,alias="contentType",)
	isInline: Optional[bool] = Field(default=None,alias="isInline",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	name: Optional[str] = Field(default=None,alias="name",)
	size: Optional[int] = Field(default=None,alias="size",)
	contentBytes: Optional[str] = Field(default=None,alias="contentBytes",)
	contentId: Optional[str] = Field(default=None,alias="contentId",)
	contentLocation: Optional[str] = Field(default=None,alias="contentLocation",)


