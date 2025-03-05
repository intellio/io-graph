from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AttachmentSession(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	content: Optional[str] = Field(default=None,alias="content",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	nextExpectedRanges: Optional[list[str]] = Field(default=None,alias="nextExpectedRanges",)


