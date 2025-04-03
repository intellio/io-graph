from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AccessReviewScheduleDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessReviewScheduleDefinition"] = Field(alias="@odata.type", default="#microsoft.graph.accessReviewScheduleDefinition")
	additionalNotificationRecipients: Optional[list[AccessReviewNotificationRecipientItem]] = Field(alias="additionalNotificationRecipients", default=None,)
	backupReviewers: Optional[list[AccessReviewReviewerScope]] = Field(alias="backupReviewers", default=None,)
	createdBy: Optional[Union[AuditUserIdentity]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	descriptionForAdmins: Optional[str] = Field(alias="descriptionForAdmins", default=None,)
	descriptionForReviewers: Optional[str] = Field(alias="descriptionForReviewers", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	fallbackReviewers: Optional[list[AccessReviewReviewerScope]] = Field(alias="fallbackReviewers", default=None,)
	instanceEnumerationScope: Optional[Union[AccessReviewInactiveUsersQueryScope, AccessReviewReviewerScope, PrincipalResourceMembershipsScope]] = Field(alias="instanceEnumerationScope", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	reviewers: Optional[list[AccessReviewReviewerScope]] = Field(alias="reviewers", default=None,)
	scope: Optional[Union[AccessReviewInactiveUsersQueryScope, AccessReviewReviewerScope, PrincipalResourceMembershipsScope]] = Field(alias="scope", default=None,discriminator="odata_type", )
	settings: Optional[AccessReviewScheduleSettings] = Field(alias="settings", default=None,)
	stageSettings: Optional[list[AccessReviewStageSettings]] = Field(alias="stageSettings", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	instances: Optional[list[AccessReviewInstance]] = Field(alias="instances", default=None,)

from .access_review_notification_recipient_item import AccessReviewNotificationRecipientItem
from .access_review_reviewer_scope import AccessReviewReviewerScope
from .audit_user_identity import AuditUserIdentity
from .access_review_inactive_users_query_scope import AccessReviewInactiveUsersQueryScope
from .principal_resource_memberships_scope import PrincipalResourceMembershipsScope
from .access_review_schedule_settings import AccessReviewScheduleSettings
from .access_review_stage_settings import AccessReviewStageSettings
from .access_review_instance import AccessReviewInstance
