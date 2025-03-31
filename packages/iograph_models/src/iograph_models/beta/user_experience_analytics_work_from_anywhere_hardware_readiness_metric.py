from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric"] = Field(alias="@odata.type",)
	osCheckFailedPercentage: float | str | ReferenceNumeric
	processor64BitCheckFailedPercentage: float | str | ReferenceNumeric
	processorCoreCountCheckFailedPercentage: float | str | ReferenceNumeric
	processorFamilyCheckFailedPercentage: float | str | ReferenceNumeric
	processorSpeedCheckFailedPercentage: float | str | ReferenceNumeric
	ramCheckFailedPercentage: float | str | ReferenceNumeric
	secureBootCheckFailedPercentage: float | str | ReferenceNumeric
	storageCheckFailedPercentage: float | str | ReferenceNumeric
	totalDeviceCount: Optional[int] = Field(alias="totalDeviceCount", default=None,)
	tpmCheckFailedPercentage: float | str | ReferenceNumeric
	upgradeEligibleDeviceCount: Optional[int] = Field(alias="upgradeEligibleDeviceCount", default=None,)

from .reference_numeric import ReferenceNumeric
