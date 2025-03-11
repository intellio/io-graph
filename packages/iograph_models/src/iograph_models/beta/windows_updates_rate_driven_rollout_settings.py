from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesRateDrivenRolloutSettings(BaseModel):
	durationBetweenOffers: Optional[str] = Field(alias="durationBetweenOffers",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	devicesPerOffer: Optional[int] = Field(alias="devicesPerOffer",default=None,)


