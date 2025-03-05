from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MultiTenantOrganizationJoinRequestRecord(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	addedByTenantId: Optional[str] = Field(alias="addedByTenantId",default=None,)
	memberState: Optional[str | MultiTenantOrganizationMemberState] = Field(alias="memberState",default=None,)
	role: Optional[str | MultiTenantOrganizationMemberRole] = Field(alias="role",default=None,)
	transitionDetails: Optional[MultiTenantOrganizationJoinRequestTransitionDetails] = Field(alias="transitionDetails",default=None,)

from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState
from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
from .multi_tenant_organization_join_request_transition_details import MultiTenantOrganizationJoinRequestTransitionDetails

