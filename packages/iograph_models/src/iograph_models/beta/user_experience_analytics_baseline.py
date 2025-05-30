from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class UserExperienceAnalyticsBaseline(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsBaseline"] = Field(alias="@odata.type", default="#microsoft.graph.userExperienceAnalyticsBaseline")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isBuiltIn: Optional[bool] = Field(alias="isBuiltIn", default=None,)
	appHealthMetrics: Optional[UserExperienceAnalyticsCategory] = Field(alias="appHealthMetrics", default=None,)
	batteryHealthMetrics: Optional[UserExperienceAnalyticsCategory] = Field(alias="batteryHealthMetrics", default=None,)
	bestPracticesMetrics: Optional[UserExperienceAnalyticsCategory] = Field(alias="bestPracticesMetrics", default=None,)
	deviceBootPerformanceMetrics: Optional[UserExperienceAnalyticsCategory] = Field(alias="deviceBootPerformanceMetrics", default=None,)
	rebootAnalyticsMetrics: Optional[UserExperienceAnalyticsCategory] = Field(alias="rebootAnalyticsMetrics", default=None,)
	resourcePerformanceMetrics: Optional[UserExperienceAnalyticsCategory] = Field(alias="resourcePerformanceMetrics", default=None,)
	workFromAnywhereMetrics: Optional[UserExperienceAnalyticsCategory] = Field(alias="workFromAnywhereMetrics", default=None,)

from .user_experience_analytics_category import UserExperienceAnalyticsCategory
