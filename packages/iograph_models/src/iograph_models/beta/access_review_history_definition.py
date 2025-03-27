from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewHistoryDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdBy: Optional[Union[AuditUserIdentity]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	decisions: Optional[list[AccessReviewHistoryDecisionFilter | str]] = Field(alias="decisions", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	downloadUri: Optional[str] = Field(alias="downloadUri", default=None,)
	fulfilledDateTime: Optional[datetime] = Field(alias="fulfilledDateTime", default=None,)
	reviewHistoryPeriodEndDateTime: Optional[datetime] = Field(alias="reviewHistoryPeriodEndDateTime", default=None,)
	reviewHistoryPeriodStartDateTime: Optional[datetime] = Field(alias="reviewHistoryPeriodStartDateTime", default=None,)
	scheduleSettings: Optional[AccessReviewHistoryScheduleSettings] = Field(alias="scheduleSettings", default=None,)
	scopes: Optional[list[Annotated[Union[AccessReviewQueryScope, AccessReviewInactiveUsersQueryScope, AccessReviewReviewerScope, PrincipalResourceMembershipsScope],Field(discriminator="odata_type")]]] = Field(alias="scopes", default=None,)
	status: Optional[AccessReviewHistoryStatus | str] = Field(alias="status", default=None,)
	instances: Optional[list[AccessReviewHistoryInstance]] = Field(alias="instances", default=None,)

from .audit_user_identity import AuditUserIdentity
from .access_review_history_decision_filter import AccessReviewHistoryDecisionFilter
from .access_review_history_schedule_settings import AccessReviewHistoryScheduleSettings
from .access_review_query_scope import AccessReviewQueryScope
from .access_review_inactive_users_query_scope import AccessReviewInactiveUsersQueryScope
from .access_review_reviewer_scope import AccessReviewReviewerScope
from .principal_resource_memberships_scope import PrincipalResourceMembershipsScope
from .access_review_history_status import AccessReviewHistoryStatus
from .access_review_history_instance import AccessReviewHistoryInstance

