from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class WindowsUpdatesDateDrivenRolloutSettings(BaseModel):
	durationBetweenOffers: Optional[str] = Field(alias="durationBetweenOffers", default=None,)
	odata_type: Literal["#microsoft.graph.windowsUpdates.dateDrivenRolloutSettings"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdates.dateDrivenRolloutSettings")
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)

