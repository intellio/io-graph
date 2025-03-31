from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TrainingCampaignReportOverview(BaseModel):
	trainingModuleCompletion: Optional[TrainingEventsContent] = Field(alias="trainingModuleCompletion", default=None,)
	trainingNotificationDeliveryStatus: Optional[TrainingNotificationDelivery] = Field(alias="trainingNotificationDeliveryStatus", default=None,)
	userCompletionStatus: Optional[UserTrainingCompletionSummary] = Field(alias="userCompletionStatus", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .training_events_content import TrainingEventsContent
from .training_notification_delivery import TrainingNotificationDelivery
from .user_training_completion_summary import UserTrainingCompletionSummary
