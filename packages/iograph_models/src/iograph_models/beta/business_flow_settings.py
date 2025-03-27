from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class BusinessFlowSettings(BaseModel):
	accessRecommendationsEnabled: Optional[bool] = Field(alias="accessRecommendationsEnabled", default=None,)
	activityDurationInDays: Optional[int] = Field(alias="activityDurationInDays", default=None,)
	autoApplyReviewResultsEnabled: Optional[bool] = Field(alias="autoApplyReviewResultsEnabled", default=None,)
	autoReviewEnabled: Optional[bool] = Field(alias="autoReviewEnabled", default=None,)
	autoReviewSettings: Optional[AutoReviewSettings] = Field(alias="autoReviewSettings", default=None,)
	justificationRequiredOnApproval: Optional[bool] = Field(alias="justificationRequiredOnApproval", default=None,)
	mailNotificationsEnabled: Optional[bool] = Field(alias="mailNotificationsEnabled", default=None,)
	recurrenceSettings: Optional[AccessReviewRecurrenceSettings] = Field(alias="recurrenceSettings", default=None,)
	remindersEnabled: Optional[bool] = Field(alias="remindersEnabled", default=None,)
	odata_type: Literal["#microsoft.graph.businessFlowSettings"] = Field(alias="@odata.type", default="#microsoft.graph.businessFlowSettings")
	durationInDays: Optional[int] = Field(alias="durationInDays", default=None,)

from .auto_review_settings import AutoReviewSettings
from .access_review_recurrence_settings import AccessReviewRecurrenceSettings

