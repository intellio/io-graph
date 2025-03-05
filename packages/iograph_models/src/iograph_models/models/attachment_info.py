from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AttachmentInfo(BaseModel):
	attachmentType: Optional[AttachmentType] = Field(default=None,alias="attachmentType",)
	contentType: Optional[str] = Field(default=None,alias="contentType",)
	name: Optional[str] = Field(default=None,alias="name",)
	size: Optional[int] = Field(default=None,alias="size",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .attachment_type import AttachmentType

