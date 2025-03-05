from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewInstance(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	fallbackReviewers: Optional[list[AccessReviewReviewerScope]] = Field(default=None,alias="fallbackReviewers",)
	reviewers: Optional[list[AccessReviewReviewerScope]] = Field(default=None,alias="reviewers",)
	scope: SerializeAsAny[Optional[AccessReviewScope]] = Field(default=None,alias="scope",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	status: Optional[str] = Field(default=None,alias="status",)
	contactedReviewers: Optional[list[AccessReviewReviewer]] = Field(default=None,alias="contactedReviewers",)
	decisions: Optional[list[AccessReviewInstanceDecisionItem]] = Field(default=None,alias="decisions",)
	stages: Optional[list[AccessReviewStage]] = Field(default=None,alias="stages",)

from .access_review_reviewer_scope import AccessReviewReviewerScope
from .access_review_reviewer_scope import AccessReviewReviewerScope
from .access_review_scope import AccessReviewScope
from .access_review_reviewer import AccessReviewReviewer
from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
from .access_review_stage import AccessReviewStage

