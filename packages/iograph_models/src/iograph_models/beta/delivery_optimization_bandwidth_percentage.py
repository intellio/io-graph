from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeliveryOptimizationBandwidthPercentage(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	maximumBackgroundBandwidthPercentage: Optional[int] = Field(alias="maximumBackgroundBandwidthPercentage",default=None,)
	maximumForegroundBandwidthPercentage: Optional[int] = Field(alias="maximumForegroundBandwidthPercentage",default=None,)


