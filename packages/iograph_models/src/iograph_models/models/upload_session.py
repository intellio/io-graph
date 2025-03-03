from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UploadSession(BaseModel):
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	nextExpectedRanges: Optional[list[str]] = Field(default=None,alias="nextExpectedRanges",)
	uploadUrl: Optional[str] = Field(default=None,alias="uploadUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


