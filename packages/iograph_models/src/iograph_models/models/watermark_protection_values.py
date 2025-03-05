from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WatermarkProtectionValues(BaseModel):
	isEnabledForContentSharing: Optional[bool] = Field(default=None,alias="isEnabledForContentSharing",)
	isEnabledForVideo: Optional[bool] = Field(default=None,alias="isEnabledForVideo",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


