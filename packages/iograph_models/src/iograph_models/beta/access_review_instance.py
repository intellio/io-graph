from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AccessReviewInstance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessReviewInstance"] = Field(alias="@odata.type",)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	errors: Optional[list[AccessReviewError]] = Field(alias="errors", default=None,)
	fallbackReviewers: Optional[list[AccessReviewReviewerScope]] = Field(alias="fallbackReviewers", default=None,)
	reviewers: Optional[list[AccessReviewReviewerScope]] = Field(alias="reviewers", default=None,)
	scope: Optional[Union[AccessReviewInactiveUsersQueryScope, AccessReviewReviewerScope, PrincipalResourceMembershipsScope]] = Field(alias="scope", default=None,discriminator="odata_type", )
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	contactedReviewers: Optional[list[AccessReviewReviewer]] = Field(alias="contactedReviewers", default=None,)
	decisions: Optional[list[AccessReviewInstanceDecisionItem]] = Field(alias="decisions", default=None,)
	definition: Optional[AccessReviewScheduleDefinition] = Field(alias="definition", default=None,)
	stages: Optional[list[AccessReviewStage]] = Field(alias="stages", default=None,)

from .access_review_error import AccessReviewError
from .access_review_reviewer_scope import AccessReviewReviewerScope
from .access_review_inactive_users_query_scope import AccessReviewInactiveUsersQueryScope
from .principal_resource_memberships_scope import PrincipalResourceMembershipsScope
from .access_review_reviewer import AccessReviewReviewer
from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
from .access_review_schedule_definition import AccessReviewScheduleDefinition
from .access_review_stage import AccessReviewStage
