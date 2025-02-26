from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class UserExperienceAnalyticsBaseline(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isBuiltIn: Optional[bool] = Field(default=None,alias="isBuiltIn",)
	appHealthMetrics: Optional[UserExperienceAnalyticsCategory] = Field(default=None,alias="appHealthMetrics",)
	batteryHealthMetrics: Optional[UserExperienceAnalyticsCategory] = Field(default=None,alias="batteryHealthMetrics",)
	bestPracticesMetrics: Optional[UserExperienceAnalyticsCategory] = Field(default=None,alias="bestPracticesMetrics",)
	deviceBootPerformanceMetrics: Optional[UserExperienceAnalyticsCategory] = Field(default=None,alias="deviceBootPerformanceMetrics",)
	rebootAnalyticsMetrics: Optional[UserExperienceAnalyticsCategory] = Field(default=None,alias="rebootAnalyticsMetrics",)
	resourcePerformanceMetrics: Optional[UserExperienceAnalyticsCategory] = Field(default=None,alias="resourcePerformanceMetrics",)
	workFromAnywhereMetrics: Optional[UserExperienceAnalyticsCategory] = Field(default=None,alias="workFromAnywhereMetrics",)

from .user_experience_analytics_category import UserExperienceAnalyticsCategory
from .user_experience_analytics_category import UserExperienceAnalyticsCategory
from .user_experience_analytics_category import UserExperienceAnalyticsCategory
from .user_experience_analytics_category import UserExperienceAnalyticsCategory
from .user_experience_analytics_category import UserExperienceAnalyticsCategory
from .user_experience_analytics_category import UserExperienceAnalyticsCategory
from .user_experience_analytics_category import UserExperienceAnalyticsCategory

