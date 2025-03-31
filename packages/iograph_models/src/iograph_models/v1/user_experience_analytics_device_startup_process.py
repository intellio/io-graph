from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsDeviceStartupProcess(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsDeviceStartupProcess"] = Field(alias="@odata.type",)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId", default=None,)
	processName: Optional[str] = Field(alias="processName", default=None,)
	productName: Optional[str] = Field(alias="productName", default=None,)
	publisher: Optional[str] = Field(alias="publisher", default=None,)
	startupImpactInMs: Optional[int] = Field(alias="startupImpactInMs", default=None,)

