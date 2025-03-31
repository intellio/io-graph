from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAnomalyCorrelationGroupOverview(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsAnomalyCorrelationGroupOverview"] = Field(alias="@odata.type",)
	anomalyCorrelationGroupCount: Optional[int] = Field(alias="anomalyCorrelationGroupCount", default=None,)
	anomalyId: Optional[str] = Field(alias="anomalyId", default=None,)
	correlationGroupAnomalousDeviceCount: Optional[int] = Field(alias="correlationGroupAnomalousDeviceCount", default=None,)
	correlationGroupAtRiskDeviceCount: Optional[int] = Field(alias="correlationGroupAtRiskDeviceCount", default=None,)
	correlationGroupDeviceCount: Optional[int] = Field(alias="correlationGroupDeviceCount", default=None,)
	correlationGroupFeatures: Optional[list[UserExperienceAnalyticsAnomalyCorrelationGroupFeature]] = Field(alias="correlationGroupFeatures", default=None,)
	correlationGroupId: Optional[str] = Field(alias="correlationGroupId", default=None,)
	correlationGroupPrevalence: Optional[UserExperienceAnalyticsAnomalyCorrelationGroupPrevalence | str] = Field(alias="correlationGroupPrevalence", default=None,)
	correlationGroupPrevalencePercentage: float | str | ReferenceNumeric
	totalDeviceCount: Optional[int] = Field(alias="totalDeviceCount", default=None,)

from .user_experience_analytics_anomaly_correlation_group_feature import UserExperienceAnalyticsAnomalyCorrelationGroupFeature
from .user_experience_analytics_anomaly_correlation_group_prevalence import UserExperienceAnalyticsAnomalyCorrelationGroupPrevalence
from .reference_numeric import ReferenceNumeric
