from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WatermarkProtectionValues(BaseModel):
	isEnabledForContentSharing: Optional[bool] = Field(alias="isEnabledForContentSharing", default=None,)
	isEnabledForVideo: Optional[bool] = Field(alias="isEnabledForVideo", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

