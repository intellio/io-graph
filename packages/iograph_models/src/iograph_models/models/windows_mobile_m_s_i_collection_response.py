from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsMobileMSICollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[WindowsMobileMSI] = Field(alias="value",)

from .windows_mobile_m_s_i import WindowsMobileMSI

