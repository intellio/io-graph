from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewHistoryDefinition(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[UserIdentity]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	decisions: Optional[AccessReviewHistoryDecisionFilter | str] = Field(alias="decisions",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	downloadUri: Optional[str] = Field(alias="downloadUri",default=None,)
	fulfilledDateTime: Optional[datetime] = Field(alias="fulfilledDateTime",default=None,)
	reviewHistoryPeriodEndDateTime: Optional[datetime] = Field(alias="reviewHistoryPeriodEndDateTime",default=None,)
	reviewHistoryPeriodStartDateTime: Optional[datetime] = Field(alias="reviewHistoryPeriodStartDateTime",default=None,)
	scheduleSettings: Optional[AccessReviewHistoryScheduleSettings] = Field(alias="scheduleSettings",default=None,)
	scopes: SerializeAsAny[Optional[list[AccessReviewScope]]] = Field(alias="scopes",default=None,)
	status: Optional[AccessReviewHistoryStatus | str] = Field(alias="status",default=None,)
	instances: Optional[list[AccessReviewHistoryInstance]] = Field(alias="instances",default=None,)

from .user_identity import UserIdentity
from .access_review_history_decision_filter import AccessReviewHistoryDecisionFilter
from .access_review_history_schedule_settings import AccessReviewHistoryScheduleSettings
from .access_review_scope import AccessReviewScope
from .access_review_history_status import AccessReviewHistoryStatus
from .access_review_history_instance import AccessReviewHistoryInstance

