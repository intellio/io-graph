from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeliveryOptimizationMaxCacheSizeAbsolute(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	maximumCacheSizeInGigabytes: Optional[int] = Field(alias="maximumCacheSizeInGigabytes",default=None,)


