from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	osCheckFailedPercentage: float | str | ReferenceNumeric
	processor64BitCheckFailedPercentage: float | str | ReferenceNumeric
	processorCoreCountCheckFailedPercentage: float | str | ReferenceNumeric
	processorFamilyCheckFailedPercentage: float | str | ReferenceNumeric
	processorSpeedCheckFailedPercentage: float | str | ReferenceNumeric
	ramCheckFailedPercentage: float | str | ReferenceNumeric
	secureBootCheckFailedPercentage: float | str | ReferenceNumeric
	storageCheckFailedPercentage: float | str | ReferenceNumeric
	totalDeviceCount: Optional[int] = Field(default=None,alias="totalDeviceCount",)
	tpmCheckFailedPercentage: float | str | ReferenceNumeric
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

