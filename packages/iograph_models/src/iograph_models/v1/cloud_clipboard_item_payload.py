from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudClipboardItemPayload(BaseModel):
	content: Optional[str] = Field(alias="content", default=None,)
	formatName: Optional[str] = Field(alias="formatName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

