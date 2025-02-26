from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	osCheckFailedPercentage: Optional[float] | Optional[str] | ReferenceNumeric
	processor64BitCheckFailedPercentage: Optional[float] | Optional[str] | ReferenceNumeric
	processorCoreCountCheckFailedPercentage: Optional[float] | Optional[str] | ReferenceNumeric
	processorFamilyCheckFailedPercentage: Optional[float] | Optional[str] | ReferenceNumeric
	processorSpeedCheckFailedPercentage: Optional[float] | Optional[str] | ReferenceNumeric
	ramCheckFailedPercentage: Optional[float] | Optional[str] | ReferenceNumeric
	secureBootCheckFailedPercentage: Optional[float] | Optional[str] | ReferenceNumeric
	storageCheckFailedPercentage: Optional[float] | Optional[str] | ReferenceNumeric
	totalDeviceCount: Optional[int] = Field(default=None,alias="totalDeviceCount",)
	tpmCheckFailedPercentage: Optional[float] | Optional[str] | ReferenceNumeric
	upgradeEligibleDeviceCount: Optional[int] = Field(default=None,alias="upgradeEligibleDeviceCount",)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

