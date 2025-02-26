from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAppHealthOSVersionPerformance(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activeDeviceCount: Optional[int] = Field(default=None,alias="activeDeviceCount",)
	meanTimeToFailureInMinutes: Optional[int] = Field(default=None,alias="meanTimeToFailureInMinutes",)
	osBuildNumber: Optional[str] = Field(default=None,alias="osBuildNumber",)
	osVersion: Optional[str] = Field(default=None,alias="osVersion",)
	osVersionAppHealthScore: Optional[float] | Optional[str] | ReferenceNumeric

from .reference_numeric import ReferenceNumeric

