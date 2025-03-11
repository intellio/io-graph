from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsDeviceScores(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appReliabilityScore: float | str | ReferenceNumeric
	batteryHealthScore: float | str | ReferenceNumeric
	deviceName: Optional[str] = Field(alias="deviceName",default=None,)
	endpointAnalyticsScore: float | str | ReferenceNumeric
	healthStatus: Optional[UserExperienceAnalyticsHealthState | str] = Field(alias="healthStatus",default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer",default=None,)
	meanResourceSpikeTimeScore: float | str | ReferenceNumeric
	model: Optional[str] = Field(alias="model",default=None,)
	startupPerformanceScore: float | str | ReferenceNumeric
	workFromAnywhereScore: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

