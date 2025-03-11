from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReview(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	businessFlowTemplateId: Optional[str] = Field(alias="businessFlowTemplateId",default=None,)
	createdBy: SerializeAsAny[Optional[UserIdentity]] = Field(alias="createdBy",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime",default=None,)
	reviewedEntity: SerializeAsAny[Optional[Identity]] = Field(alias="reviewedEntity",default=None,)
	reviewerType: Optional[str] = Field(alias="reviewerType",default=None,)
	settings: SerializeAsAny[Optional[AccessReviewSettings]] = Field(alias="settings",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	status: Optional[str] = Field(alias="status",default=None,)
	decisions: Optional[list[AccessReviewDecision]] = Field(alias="decisions",default=None,)
	instances: Optional[list[AccessReview]] = Field(alias="instances",default=None,)
	myDecisions: Optional[list[AccessReviewDecision]] = Field(alias="myDecisions",default=None,)
	reviewers: Optional[list[AccessReviewReviewer]] = Field(alias="reviewers",default=None,)

from .user_identity import UserIdentity
from .identity import Identity
from .access_review_settings import AccessReviewSettings
from .access_review_decision import AccessReviewDecision
from .access_review_decision import AccessReviewDecision
from .access_review_reviewer import AccessReviewReviewer

