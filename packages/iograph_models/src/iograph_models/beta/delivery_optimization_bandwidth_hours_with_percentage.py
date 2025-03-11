from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeliveryOptimizationBandwidthHoursWithPercentage(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	bandwidthBackgroundPercentageHours: Optional[DeliveryOptimizationBandwidthBusinessHoursLimit] = Field(alias="bandwidthBackgroundPercentageHours",default=None,)
	bandwidthForegroundPercentageHours: Optional[DeliveryOptimizationBandwidthBusinessHoursLimit] = Field(alias="bandwidthForegroundPercentageHours",default=None,)

from .delivery_optimization_bandwidth_business_hours_limit import DeliveryOptimizationBandwidthBusinessHoursLimit
from .delivery_optimization_bandwidth_business_hours_limit import DeliveryOptimizationBandwidthBusinessHoursLimit

