from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class EngagementUploadSession(BaseModel):
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	nextExpectedRanges: Optional[list[str]] = Field(alias="nextExpectedRanges", default=None,)
	uploadUrl: Optional[str] = Field(alias="uploadUrl", default=None,)
	odata_type: Literal["#microsoft.graph.engagementUploadSession"] = Field(alias="@odata.type",)
	id: Optional[str] = Field(alias="id", default=None,)

