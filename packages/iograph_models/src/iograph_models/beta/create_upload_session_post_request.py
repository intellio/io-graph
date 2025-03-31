from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Create_upload_sessionPostRequest(BaseModel):
	attachmentInfo: Optional[AttachmentInfo] = Field(alias="attachmentInfo", default=None,)

from .attachment_info import AttachmentInfo
