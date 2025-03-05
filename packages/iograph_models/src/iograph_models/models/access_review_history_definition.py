from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewHistoryDefinition(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[UserIdentity] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	decisions: Optional[AccessReviewHistoryDecisionFilter] = Field(default=None,alias="decisions",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	reviewHistoryPeriodEndDateTime: Optional[datetime] = Field(default=None,alias="reviewHistoryPeriodEndDateTime",)
	reviewHistoryPeriodStartDateTime: Optional[datetime] = Field(default=None,alias="reviewHistoryPeriodStartDateTime",)
	scheduleSettings: Optional[AccessReviewHistoryScheduleSettings] = Field(default=None,alias="scheduleSettings",)
	scopes: SerializeAsAny[Optional[list[AccessReviewScope]]] = Field(default=None,alias="scopes",)
	status: Optional[AccessReviewHistoryStatus] = Field(default=None,alias="status",)
	instances: Optional[list[AccessReviewHistoryInstance]] = Field(default=None,alias="instances",)

from .user_identity import UserIdentity
from .access_review_history_decision_filter import AccessReviewHistoryDecisionFilter
from .access_review_history_schedule_settings import AccessReviewHistoryScheduleSettings
from .access_review_scope import AccessReviewScope
from .access_review_history_status import AccessReviewHistoryStatus
from .access_review_history_instance import AccessReviewHistoryInstance

