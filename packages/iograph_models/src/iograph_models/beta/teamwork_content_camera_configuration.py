from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkContentCameraConfiguration(BaseModel):
	isContentCameraInverted: Optional[bool] = Field(alias="isContentCameraInverted",default=None,)
	isContentCameraOptional: Optional[bool] = Field(alias="isContentCameraOptional",default=None,)
	isContentEnhancementEnabled: Optional[bool] = Field(alias="isContentEnhancementEnabled",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


