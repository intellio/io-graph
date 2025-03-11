from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsDeviceStartupProcessPerformance(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deviceCount: Optional[int] = Field(alias="deviceCount",default=None,)
	medianImpactInMs: Optional[int] = Field(alias="medianImpactInMs",default=None,)
	processName: Optional[str] = Field(alias="processName",default=None,)
	productName: Optional[str] = Field(alias="productName",default=None,)
	publisher: Optional[str] = Field(alias="publisher",default=None,)
	totalImpactInMs: Optional[int] = Field(alias="totalImpactInMs",default=None,)


