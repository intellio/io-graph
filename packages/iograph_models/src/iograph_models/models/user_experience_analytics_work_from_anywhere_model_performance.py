from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsWorkFromAnywhereModelPerformance(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	cloudIdentityScore: float | str | ReferenceNumeric
	cloudManagementScore: float | str | ReferenceNumeric
	cloudProvisioningScore: float | str | ReferenceNumeric
	healthStatus: Optional[str | UserExperienceAnalyticsHealthState] = Field(alias="healthStatus",default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer",default=None,)
	model: Optional[str] = Field(alias="model",default=None,)
	modelDeviceCount: Optional[int] = Field(alias="modelDeviceCount",default=None,)
	windowsScore: float | str | ReferenceNumeric
	workFromAnywhereScore: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

