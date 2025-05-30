from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SearchResult(BaseModel):
	onClickTelemetryUrl: Optional[str] = Field(alias="onClickTelemetryUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

