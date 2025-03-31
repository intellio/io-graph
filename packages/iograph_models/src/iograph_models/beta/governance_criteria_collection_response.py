from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class GovernanceCriteriaCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[GroupMembershipGovernanceCriteria, RoleMembershipGovernanceCriteria, UserGovernanceCriteria],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .group_membership_governance_criteria import GroupMembershipGovernanceCriteria
from .role_membership_governance_criteria import RoleMembershipGovernanceCriteria
from .user_governance_criteria import UserGovernanceCriteria
