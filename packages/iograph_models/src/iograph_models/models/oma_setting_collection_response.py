from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OmaSettingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[OmaSetting] = Field(alias="value",)

from .oma_setting import OmaSetting

