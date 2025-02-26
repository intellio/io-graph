from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AttachmentItem(BaseModel):
	attachmentType: Optional[AttachmentType] = Field(default=None,alias="attachmentType",)
	contentId: Optional[str] = Field(default=None,alias="contentId",)
	contentType: Optional[str] = Field(default=None,alias="contentType",)
	isInline: Optional[bool] = Field(default=None,alias="isInline",)
	name: Optional[str] = Field(default=None,alias="name",)
	size: Optional[int] = Field(default=None,alias="size",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .attachment_type import AttachmentType

