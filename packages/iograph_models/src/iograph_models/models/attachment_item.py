from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AttachmentItem(BaseModel):
	attachmentType: Optional[str | AttachmentType] = Field(alias="attachmentType",default=None,)
	contentId: Optional[str] = Field(alias="contentId",default=None,)
	contentType: Optional[str] = Field(alias="contentType",default=None,)
	isInline: Optional[bool] = Field(alias="isInline",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	size: Optional[int] = Field(alias="size",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .attachment_type import AttachmentType

