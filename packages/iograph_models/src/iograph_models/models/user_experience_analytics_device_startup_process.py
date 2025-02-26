from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserExperienceAnalyticsDeviceStartupProcess(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	managedDeviceId: Optional[str] = Field(default=None,alias="managedDeviceId",)
	processName: Optional[str] = Field(default=None,alias="processName",)
	productName: Optional[str] = Field(default=None,alias="productName",)
	publisher: Optional[str] = Field(default=None,alias="publisher",)
	startupImpactInMs: Optional[int] = Field(default=None,alias="startupImpactInMs",)


