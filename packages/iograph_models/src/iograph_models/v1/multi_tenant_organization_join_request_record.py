from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MultiTenantOrganizationJoinRequestRecord(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.multiTenantOrganizationJoinRequestRecord"] = Field(alias="@odata.type",)
	addedByTenantId: Optional[str] = Field(alias="addedByTenantId", default=None,)
	memberState: Optional[MultiTenantOrganizationMemberState | str] = Field(alias="memberState", default=None,)
	role: Optional[MultiTenantOrganizationMemberRole | str] = Field(alias="role", default=None,)
	transitionDetails: Optional[MultiTenantOrganizationJoinRequestTransitionDetails] = Field(alias="transitionDetails", default=None,)

from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState
from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
from .multi_tenant_organization_join_request_transition_details import MultiTenantOrganizationJoinRequestTransitionDetails
