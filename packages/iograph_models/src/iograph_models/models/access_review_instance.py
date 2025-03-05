from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewInstance(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime",default=None,)
	fallbackReviewers: Optional[list[AccessReviewReviewerScope]] = Field(alias="fallbackReviewers",default=None,)
	reviewers: Optional[list[AccessReviewReviewerScope]] = Field(alias="reviewers",default=None,)
	scope: SerializeAsAny[Optional[AccessReviewScope]] = Field(alias="scope",default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime",default=None,)
	status: Optional[str] = Field(alias="status",default=None,)
	contactedReviewers: Optional[list[AccessReviewReviewer]] = Field(alias="contactedReviewers",default=None,)
	decisions: Optional[list[AccessReviewInstanceDecisionItem]] = Field(alias="decisions",default=None,)
	stages: Optional[list[AccessReviewStage]] = Field(alias="stages",default=None,)

from .access_review_reviewer_scope import AccessReviewReviewerScope
from .access_review_reviewer_scope import AccessReviewReviewerScope
from .access_review_scope import AccessReviewScope
from .access_review_reviewer import AccessReviewReviewer
from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
from .access_review_stage import AccessReviewStage

