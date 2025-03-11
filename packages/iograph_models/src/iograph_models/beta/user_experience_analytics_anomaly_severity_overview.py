from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsAnomalySeverityOverview(BaseModel):
	highSeverityAnomalyCount: Optional[int] = Field(alias="highSeverityAnomalyCount",default=None,)
	informationalSeverityAnomalyCount: Optional[int] = Field(alias="informationalSeverityAnomalyCount",default=None,)
	lowSeverityAnomalyCount: Optional[int] = Field(alias="lowSeverityAnomalyCount",default=None,)
	mediumSeverityAnomalyCount: Optional[int] = Field(alias="mediumSeverityAnomalyCount",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


