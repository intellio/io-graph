from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeliveryOptimizationBandwidthPercentage(BaseModel):
	odata_type: Literal["#microsoft.graph.deliveryOptimizationBandwidthPercentage"] = Field(alias="@odata.type", default="#microsoft.graph.deliveryOptimizationBandwidthPercentage")
	maximumBackgroundBandwidthPercentage: Optional[int] = Field(alias="maximumBackgroundBandwidthPercentage", default=None,)
	maximumForegroundBandwidthPercentage: Optional[int] = Field(alias="maximumForegroundBandwidthPercentage", default=None,)

