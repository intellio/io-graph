from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AdminConsentRequestPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	notifyReviewers: Optional[bool] = Field(default=None,alias="notifyReviewers",)
	remindersEnabled: Optional[bool] = Field(default=None,alias="remindersEnabled",)
	requestDurationInDays: Optional[int] = Field(default=None,alias="requestDurationInDays",)
	reviewers: list[AccessReviewReviewerScope] = Field(alias="reviewers",)
	version: Optional[int] = Field(default=None,alias="version",)

from .access_review_reviewer_scope import AccessReviewReviewerScope

