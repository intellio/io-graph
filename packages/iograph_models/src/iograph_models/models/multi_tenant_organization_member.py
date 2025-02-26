from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MultiTenantOrganizationMember(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	addedByTenantId: Optional[UUID] = Field(default=None,alias="addedByTenantId",)
	addedDateTime: Optional[datetime] = Field(default=None,alias="addedDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	joinedDateTime: Optional[datetime] = Field(default=None,alias="joinedDateTime",)
	role: Optional[MultiTenantOrganizationMemberRole] = Field(default=None,alias="role",)
	state: Optional[MultiTenantOrganizationMemberState] = Field(default=None,alias="state",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	transitionDetails: Optional[MultiTenantOrganizationMemberTransitionDetails] = Field(default=None,alias="transitionDetails",)

from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState
from .multi_tenant_organization_member_transition_details import MultiTenantOrganizationMemberTransitionDetails

