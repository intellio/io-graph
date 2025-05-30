from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class FileAttachment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.fileAttachment"] = Field(alias="@odata.type", default="#microsoft.graph.fileAttachment")
	contentType: Optional[str] = Field(alias="contentType", default=None,)
	isInline: Optional[bool] = Field(alias="isInline", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	size: Optional[int] = Field(alias="size", default=None,)
	contentBytes: Optional[str] = Field(alias="contentBytes", default=None,)
	contentId: Optional[str] = Field(alias="contentId", default=None,)
	contentLocation: Optional[str] = Field(alias="contentLocation", default=None,)

