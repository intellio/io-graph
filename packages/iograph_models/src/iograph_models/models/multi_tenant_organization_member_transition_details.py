from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MultiTenantOrganizationMemberTransitionDetails(BaseModel):
	desiredRole: Optional[MultiTenantOrganizationMemberRole] = Field(default=None,alias="desiredRole",)
	desiredState: Optional[MultiTenantOrganizationMemberState] = Field(default=None,alias="desiredState",)
	details: Optional[str] = Field(default=None,alias="details",)
	status: Optional[MultiTenantOrganizationMemberProcessingStatus] = Field(default=None,alias="status",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState
from .multi_tenant_organization_member_processing_status import MultiTenantOrganizationMemberProcessingStatus

