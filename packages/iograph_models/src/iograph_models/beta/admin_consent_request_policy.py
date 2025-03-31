from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AdminConsentRequestPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.adminConsentRequestPolicy"] = Field(alias="@odata.type",)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	notifyReviewers: Optional[bool] = Field(alias="notifyReviewers", default=None,)
	remindersEnabled: Optional[bool] = Field(alias="remindersEnabled", default=None,)
	requestDurationInDays: Optional[int] = Field(alias="requestDurationInDays", default=None,)
	reviewers: Optional[list[AccessReviewReviewerScope]] = Field(alias="reviewers", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)

from .access_review_reviewer_scope import AccessReviewReviewerScope
