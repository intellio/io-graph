from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class AssignmentReviewSettings(BaseModel):
	accessReviewTimeoutBehavior: Optional[AccessReviewTimeoutBehavior | str] = Field(alias="accessReviewTimeoutBehavior", default=None,)
	durationInDays: Optional[int] = Field(alias="durationInDays", default=None,)
	isAccessRecommendationEnabled: Optional[bool] = Field(alias="isAccessRecommendationEnabled", default=None,)
	isApprovalJustificationRequired: Optional[bool] = Field(alias="isApprovalJustificationRequired", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	recurrenceType: Optional[str] = Field(alias="recurrenceType", default=None,)
	reviewers: Optional[list[Annotated[Union[ConnectedOrganizationMembers, ExternalSponsors, GroupMembers, InternalSponsors, RequestorManager, SingleUser, TargetUserSponsors],Field(discriminator="odata_type")]]] = Field(alias="reviewers", default=None,)
	reviewerType: Optional[str] = Field(alias="reviewerType", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .access_review_timeout_behavior import AccessReviewTimeoutBehavior
from .connected_organization_members import ConnectedOrganizationMembers
from .external_sponsors import ExternalSponsors
from .group_members import GroupMembers
from .internal_sponsors import InternalSponsors
from .requestor_manager import RequestorManager
from .single_user import SingleUser
from .target_user_sponsors import TargetUserSponsors
