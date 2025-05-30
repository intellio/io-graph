from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LiveCaptionOptions(BaseModel):
	streamUrl: Optional[str] = Field(alias="streamUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

