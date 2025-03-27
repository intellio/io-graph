from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class GovernancePolicy(BaseModel):
	decisionMakerCriteria: Optional[list[Annotated[Union[GroupMembershipGovernanceCriteria, RoleMembershipGovernanceCriteria, UserGovernanceCriteria],Field(discriminator="odata_type")]]] = Field(alias="decisionMakerCriteria", default=None,)
	notificationPolicy: Optional[GovernanceNotificationPolicy] = Field(alias="notificationPolicy", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .group_membership_governance_criteria import GroupMembershipGovernanceCriteria
from .role_membership_governance_criteria import RoleMembershipGovernanceCriteria
from .user_governance_criteria import UserGovernanceCriteria
from .governance_notification_policy import GovernanceNotificationPolicy

