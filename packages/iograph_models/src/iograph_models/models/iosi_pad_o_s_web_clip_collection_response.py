from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosiPadOSWebClipCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[IosiPadOSWebClip] = Field(alias="value",)

from .iosi_pad_o_s_web_clip import IosiPadOSWebClip

