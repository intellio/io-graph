from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MicrosoftPersonalizationSettings(BaseModel):
	isBingRewardsFeatureEnabled: Optional[bool] = Field(alias="isBingRewardsFeatureEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

