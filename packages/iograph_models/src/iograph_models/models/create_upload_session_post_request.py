from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Create_upload_sessionPostRequest(BaseModel):
	attachmentInfo: Optional[AttachmentInfo] = Field(default=None,alias="attachmentInfo",)

from .attachment_info import AttachmentInfo

