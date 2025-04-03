from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class UserExperienceAnalyticsAnomaly(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsAnomaly"] = Field(alias="@odata.type", default="#microsoft.graph.userExperienceAnalyticsAnomaly")
	anomalyFirstOccurrenceDateTime: Optional[datetime] = Field(alias="anomalyFirstOccurrenceDateTime", default=None,)
	anomalyId: Optional[str] = Field(alias="anomalyId", default=None,)
	anomalyLatestOccurrenceDateTime: Optional[datetime] = Field(alias="anomalyLatestOccurrenceDateTime", default=None,)
	anomalyName: Optional[str] = Field(alias="anomalyName", default=None,)
	anomalyType: Optional[UserExperienceAnalyticsAnomalyType | str] = Field(alias="anomalyType", default=None,)
	assetName: Optional[str] = Field(alias="assetName", default=None,)
	assetPublisher: Optional[str] = Field(alias="assetPublisher", default=None,)
	assetVersion: Optional[str] = Field(alias="assetVersion", default=None,)
	detectionModelId: Optional[str] = Field(alias="detectionModelId", default=None,)
	deviceImpactedCount: Optional[int] = Field(alias="deviceImpactedCount", default=None,)
	issueId: Optional[str] = Field(alias="issueId", default=None,)
	severity: Optional[UserExperienceAnalyticsAnomalySeverity | str] = Field(alias="severity", default=None,)
	state: Optional[UserExperienceAnalyticsAnomalyState | str] = Field(alias="state", default=None,)

from .user_experience_analytics_anomaly_type import UserExperienceAnalyticsAnomalyType
from .user_experience_analytics_anomaly_severity import UserExperienceAnalyticsAnomalySeverity
from .user_experience_analytics_anomaly_state import UserExperienceAnalyticsAnomalyState
