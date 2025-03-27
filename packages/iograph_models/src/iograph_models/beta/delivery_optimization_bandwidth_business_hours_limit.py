from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeliveryOptimizationBandwidthBusinessHoursLimit(BaseModel):
	bandwidthBeginBusinessHours: Optional[int] = Field(alias="bandwidthBeginBusinessHours", default=None,)
	bandwidthEndBusinessHours: Optional[int] = Field(alias="bandwidthEndBusinessHours", default=None,)
	bandwidthPercentageDuringBusinessHours: Optional[int] = Field(alias="bandwidthPercentageDuringBusinessHours", default=None,)
	bandwidthPercentageOutsideBusinessHours: Optional[int] = Field(alias="bandwidthPercentageOutsideBusinessHours", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


