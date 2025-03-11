from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EngagementUploadSession(BaseModel):
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	nextExpectedRanges: Optional[list[str]] = Field(alias="nextExpectedRanges",default=None,)
	uploadUrl: Optional[str] = Field(alias="uploadUrl",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)


