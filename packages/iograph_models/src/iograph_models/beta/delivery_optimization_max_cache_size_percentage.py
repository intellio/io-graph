from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeliveryOptimizationMaxCacheSizePercentage(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	maximumCacheSizePercentage: Optional[int] = Field(alias="maximumCacheSizePercentage",default=None,)


