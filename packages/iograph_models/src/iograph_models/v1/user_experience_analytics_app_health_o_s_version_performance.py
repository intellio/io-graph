from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAppHealthOSVersionPerformance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsAppHealthOSVersionPerformance"] = Field(alias="@odata.type", default="#microsoft.graph.userExperienceAnalyticsAppHealthOSVersionPerformance")
	activeDeviceCount: Optional[int] = Field(alias="activeDeviceCount", default=None,)
	meanTimeToFailureInMinutes: Optional[int] = Field(alias="meanTimeToFailureInMinutes", default=None,)
	osBuildNumber: Optional[str] = Field(alias="osBuildNumber", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	osVersionAppHealthScore: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
