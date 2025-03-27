from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesRateDrivenRolloutSettings(BaseModel):
	durationBetweenOffers: Optional[str] = Field(alias="durationBetweenOffers", default=None,)
	odata_type: Literal["#microsoft.graph.windowsUpdates.rateDrivenRolloutSettings"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdates.rateDrivenRolloutSettings")
	devicesPerOffer: Optional[int] = Field(alias="devicesPerOffer", default=None,)


