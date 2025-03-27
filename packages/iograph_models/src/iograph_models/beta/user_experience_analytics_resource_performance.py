from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsResourcePerformance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	averageSpikeTimeScore: Optional[int] = Field(alias="averageSpikeTimeScore", default=None,)
	cpuClockSpeedInMHz: float | str | ReferenceNumeric
	cpuDisplayName: Optional[str] = Field(alias="cpuDisplayName", default=None,)
	cpuSpikeTimePercentage: float | str | ReferenceNumeric
	cpuSpikeTimePercentageThreshold: float | str | ReferenceNumeric
	cpuSpikeTimeScore: Optional[int] = Field(alias="cpuSpikeTimeScore", default=None,)
	deviceCount: Optional[int] = Field(alias="deviceCount", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	deviceResourcePerformanceScore: Optional[int] = Field(alias="deviceResourcePerformanceScore", default=None,)
	diskType: Optional[DiskType | str] = Field(alias="diskType", default=None,)
	healthStatus: Optional[UserExperienceAnalyticsHealthState | str] = Field(alias="healthStatus", default=None,)
	machineType: Optional[UserExperienceAnalyticsMachineType | str] = Field(alias="machineType", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	ramSpikeTimePercentage: float | str | ReferenceNumeric
	ramSpikeTimePercentageThreshold: float | str | ReferenceNumeric
	ramSpikeTimeScore: Optional[int] = Field(alias="ramSpikeTimeScore", default=None,)
	totalProcessorCoreCount: Optional[int] = Field(alias="totalProcessorCoreCount", default=None,)
	totalRamInMB: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .disk_type import DiskType
from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
from .user_experience_analytics_machine_type import UserExperienceAnalyticsMachineType
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

