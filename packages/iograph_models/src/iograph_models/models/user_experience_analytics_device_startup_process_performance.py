from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsDeviceStartupProcessPerformance(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deviceCount: Optional[int] = Field(default=None,alias="deviceCount",)
	medianImpactInMs: Optional[int] = Field(default=None,alias="medianImpactInMs",)
	processName: Optional[str] = Field(default=None,alias="processName",)
	productName: Optional[str] = Field(default=None,alias="productName",)
	publisher: Optional[str] = Field(default=None,alias="publisher",)
	totalImpactInMs: Optional[int] = Field(default=None,alias="totalImpactInMs",)


