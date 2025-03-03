from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AccessReviewScheduleDefinition(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	additionalNotificationRecipients: Optional[list[AccessReviewNotificationRecipientItem]] = Field(default=None,alias="additionalNotificationRecipients",)
	createdBy: Optional[UserIdentity] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	descriptionForAdmins: Optional[str] = Field(default=None,alias="descriptionForAdmins",)
	descriptionForReviewers: Optional[str] = Field(default=None,alias="descriptionForReviewers",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	fallbackReviewers: Optional[list[AccessReviewReviewerScope]] = Field(default=None,alias="fallbackReviewers",)
	instanceEnumerationScope: Optional[AccessReviewScope] = Field(default=None,alias="instanceEnumerationScope",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	reviewers: Optional[list[AccessReviewReviewerScope]] = Field(default=None,alias="reviewers",)
	scope: Optional[AccessReviewScope] = Field(default=None,alias="scope",)
	settings: Optional[AccessReviewScheduleSettings] = Field(default=None,alias="settings",)
	stageSettings: Optional[list[AccessReviewStageSettings]] = Field(default=None,alias="stageSettings",)
	status: Optional[str] = Field(default=None,alias="status",)
	instances: Optional[list[AccessReviewInstance]] = Field(default=None,alias="instances",)

from .access_review_notification_recipient_item import AccessReviewNotificationRecipientItem
from .user_identity import UserIdentity
from .access_review_reviewer_scope import AccessReviewReviewerScope
from .access_review_scope import AccessReviewScope
from .access_review_reviewer_scope import AccessReviewReviewerScope
from .access_review_scope import AccessReviewScope
from .access_review_schedule_settings import AccessReviewScheduleSettings
from .access_review_stage_settings import AccessReviewStageSettings
from .access_review_instance import AccessReviewInstance

