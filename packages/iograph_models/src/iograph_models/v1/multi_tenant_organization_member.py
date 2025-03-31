from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MultiTenantOrganizationMember(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.multiTenantOrganizationMember"] = Field(alias="@odata.type", default="#microsoft.graph.multiTenantOrganizationMember")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	addedByTenantId: Optional[UUID] = Field(alias="addedByTenantId", default=None,)
	addedDateTime: Optional[datetime] = Field(alias="addedDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	joinedDateTime: Optional[datetime] = Field(alias="joinedDateTime", default=None,)
	role: Optional[MultiTenantOrganizationMemberRole | str] = Field(alias="role", default=None,)
	state: Optional[MultiTenantOrganizationMemberState | str] = Field(alias="state", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	transitionDetails: Optional[MultiTenantOrganizationMemberTransitionDetails] = Field(alias="transitionDetails", default=None,)

from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState
from .multi_tenant_organization_member_transition_details import MultiTenantOrganizationMemberTransitionDetails
