from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeliveryOptimizationMaxCacheSizeAbsolute(BaseModel):
	odata_type: Literal["#microsoft.graph.deliveryOptimizationMaxCacheSizeAbsolute"] = Field(alias="@odata.type", default="#microsoft.graph.deliveryOptimizationMaxCacheSizeAbsolute")
	maximumCacheSizeInGigabytes: Optional[int] = Field(alias="maximumCacheSizeInGigabytes", default=None,)

