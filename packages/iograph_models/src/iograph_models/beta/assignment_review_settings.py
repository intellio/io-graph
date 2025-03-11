from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AssignmentReviewSettings(BaseModel):
	accessReviewTimeoutBehavior: Optional[AccessReviewTimeoutBehavior | str] = Field(alias="accessReviewTimeoutBehavior",default=None,)
	durationInDays: Optional[int] = Field(alias="durationInDays",default=None,)
	isAccessRecommendationEnabled: Optional[bool] = Field(alias="isAccessRecommendationEnabled",default=None,)
	isApprovalJustificationRequired: Optional[bool] = Field(alias="isApprovalJustificationRequired",default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	recurrenceType: Optional[str] = Field(alias="recurrenceType",default=None,)
	reviewers: SerializeAsAny[Optional[list[UserSet]]] = Field(alias="reviewers",default=None,)
	reviewerType: Optional[str] = Field(alias="reviewerType",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .access_review_timeout_behavior import AccessReviewTimeoutBehavior
from .user_set import UserSet

