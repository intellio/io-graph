from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AccessReviewStage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	fallbackReviewers: list[AccessReviewReviewerScope] = Field(alias="fallbackReviewers",)
	reviewers: list[AccessReviewReviewerScope] = Field(alias="reviewers",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	status: Optional[str] = Field(default=None,alias="status",)
	decisions: list[AccessReviewInstanceDecisionItem] = Field(alias="decisions",)

from .access_review_reviewer_scope import AccessReviewReviewerScope
from .access_review_reviewer_scope import AccessReviewReviewerScope
from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem

