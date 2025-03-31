from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AttachmentSession(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.attachmentSession"] = Field(alias="@odata.type",)
	content: Optional[str] = Field(alias="content", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	nextExpectedRanges: Optional[list[str]] = Field(alias="nextExpectedRanges", default=None,)

