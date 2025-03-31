from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MediaInfo(BaseModel):
	resourceId: Optional[str] = Field(alias="resourceId", default=None,)
	uri: Optional[str] = Field(alias="uri", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

