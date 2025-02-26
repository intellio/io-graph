from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AccessReviewScheduleDefinition(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	additionalNotificationRecipients: list[AccessReviewNotificationRecipientItem] = Field(alias="additionalNotificationRecipients",)
	createdBy: Optional[UserIdentity] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	descriptionForAdmins: Optional[str] = Field(default=None,alias="descriptionForAdmins",)
	descriptionForReviewers: Optional[str] = Field(default=None,alias="descriptionForReviewers",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	fallbackReviewers: list[AccessReviewReviewerScope] = Field(alias="fallbackReviewers",)
	instanceEnumerationScope: Optional[AccessReviewScope] = Field(default=None,alias="instanceEnumerationScope",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	reviewers: list[AccessReviewReviewerScope] = Field(alias="reviewers",)
	scope: Optional[AccessReviewScope] = Field(default=None,alias="scope",)
	settings: Optional[AccessReviewScheduleSettings] = Field(default=None,alias="settings",)
	stageSettings: list[AccessReviewStageSettings] = Field(alias="stageSettings",)
	status: Optional[str] = Field(default=None,alias="status",)
	instances: list[AccessReviewInstance] = Field(alias="instances",)

from .access_review_notification_recipient_item import AccessReviewNotificationRecipientItem
from .user_identity import UserIdentity
from .access_review_reviewer_scope import AccessReviewReviewerScope
from .access_review_scope import AccessReviewScope
from .access_review_reviewer_scope import AccessReviewReviewerScope
from .access_review_scope import AccessReviewScope
from .access_review_schedule_settings import AccessReviewScheduleSettings
from .access_review_stage_settings import AccessReviewStageSettings
from .access_review_instance import AccessReviewInstance

