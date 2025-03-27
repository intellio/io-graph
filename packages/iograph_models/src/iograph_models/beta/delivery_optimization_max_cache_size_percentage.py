from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeliveryOptimizationMaxCacheSizePercentage(BaseModel):
	odata_type: Literal["#microsoft.graph.deliveryOptimizationMaxCacheSizePercentage"] = Field(alias="@odata.type", default="#microsoft.graph.deliveryOptimizationMaxCacheSizePercentage")
	maximumCacheSizePercentage: Optional[int] = Field(alias="maximumCacheSizePercentage", default=None,)


