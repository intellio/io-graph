from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeliveryOptimizationBandwidthAbsolute(BaseModel):
	odata_type: Literal["#microsoft.graph.deliveryOptimizationBandwidthAbsolute"] = Field(alias="@odata.type", default="#microsoft.graph.deliveryOptimizationBandwidthAbsolute")
	maximumDownloadBandwidthInKilobytesPerSecond: Optional[int] = Field(alias="maximumDownloadBandwidthInKilobytesPerSecond", default=None,)
	maximumUploadBandwidthInKilobytesPerSecond: Optional[int] = Field(alias="maximumUploadBandwidthInKilobytesPerSecond", default=None,)

