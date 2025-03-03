from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalConnectorsUrlMatchInfo(BaseModel):
	baseUrls: Optional[list[str]] = Field(default=None,alias="baseUrls",)
	urlPattern: Optional[str] = Field(default=None,alias="urlPattern",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


