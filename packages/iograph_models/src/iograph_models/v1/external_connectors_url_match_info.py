from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalConnectorsUrlMatchInfo(BaseModel):
	baseUrls: Optional[list[str]] = Field(alias="baseUrls", default=None,)
	urlPattern: Optional[str] = Field(alias="urlPattern", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

