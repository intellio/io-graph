from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MultiTenantOrganizationJoinRequestRecord(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	addedByTenantId: Optional[str] = Field(default=None,alias="addedByTenantId",)
	memberState: Optional[MultiTenantOrganizationMemberState] = Field(default=None,alias="memberState",)
	role: Optional[MultiTenantOrganizationMemberRole] = Field(default=None,alias="role",)
	transitionDetails: Optional[MultiTenantOrganizationJoinRequestTransitionDetails] = Field(default=None,alias="transitionDetails",)

from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState
from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
from .multi_tenant_organization_join_request_transition_details import MultiTenantOrganizationJoinRequestTransitionDetails

