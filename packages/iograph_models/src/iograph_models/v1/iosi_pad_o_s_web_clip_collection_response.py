from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosiPadOSWebClipCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IosiPadOSWebClip]] = Field(alias="value", default=None,)

from .iosi_pad_o_s_web_clip import IosiPadOSWebClip

