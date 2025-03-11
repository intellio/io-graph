from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeliveryOptimizationBandwidthAbsolute(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	maximumDownloadBandwidthInKilobytesPerSecond: Optional[int] = Field(alias="maximumDownloadBandwidthInKilobytesPerSecond",default=None,)
	maximumUploadBandwidthInKilobytesPerSecond: Optional[int] = Field(alias="maximumUploadBandwidthInKilobytesPerSecond",default=None,)


