from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAssignmentReviewSettings(BaseModel):
	expirationBehavior: Optional[AccessReviewExpirationBehavior] = Field(default=None,alias="expirationBehavior",)
	fallbackReviewers: SerializeAsAny[Optional[list[SubjectSet]]] = Field(default=None,alias="fallbackReviewers",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	isRecommendationEnabled: Optional[bool] = Field(default=None,alias="isRecommendationEnabled",)
	isReviewerJustificationRequired: Optional[bool] = Field(default=None,alias="isReviewerJustificationRequired",)
	isSelfReview: Optional[bool] = Field(default=None,alias="isSelfReview",)
	primaryReviewers: SerializeAsAny[Optional[list[SubjectSet]]] = Field(default=None,alias="primaryReviewers",)
	schedule: Optional[EntitlementManagementSchedule] = Field(default=None,alias="schedule",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .access_review_expiration_behavior import AccessReviewExpirationBehavior
from .subject_set import SubjectSet
from .subject_set import SubjectSet
from .entitlement_management_schedule import EntitlementManagementSchedule

