from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageAssignmentReviewSettings(BaseModel):
	expirationBehavior: Optional[AccessReviewExpirationBehavior | str] = Field(alias="expirationBehavior",default=None,)
	fallbackReviewers: SerializeAsAny[Optional[list[SubjectSet]]] = Field(alias="fallbackReviewers",default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	isRecommendationEnabled: Optional[bool] = Field(alias="isRecommendationEnabled",default=None,)
	isReviewerJustificationRequired: Optional[bool] = Field(alias="isReviewerJustificationRequired",default=None,)
	isSelfReview: Optional[bool] = Field(alias="isSelfReview",default=None,)
	primaryReviewers: SerializeAsAny[Optional[list[SubjectSet]]] = Field(alias="primaryReviewers",default=None,)
	schedule: Optional[EntitlementManagementSchedule] = Field(alias="schedule",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .access_review_expiration_behavior import AccessReviewExpirationBehavior
from .subject_set import SubjectSet
from .subject_set import SubjectSet
from .entitlement_management_schedule import EntitlementManagementSchedule

