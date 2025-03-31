from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsDeviceScopeSummary(BaseModel):
	completedDeviceScopeIds: Optional[list[str]] = Field(alias="completedDeviceScopeIds", default=None,)
	insufficientDataDeviceScopeIds: Optional[list[str]] = Field(alias="insufficientDataDeviceScopeIds", default=None,)
	totalDeviceScopes: Optional[int] = Field(alias="totalDeviceScopes", default=None,)
	totalDeviceScopesEnabled: Optional[int] = Field(alias="totalDeviceScopesEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

