from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MultiTenantOrganizationMemberTransitionDetails(BaseModel):
	desiredRole: Optional[str | MultiTenantOrganizationMemberRole] = Field(alias="desiredRole",default=None,)
	desiredState: Optional[str | MultiTenantOrganizationMemberState] = Field(alias="desiredState",default=None,)
	details: Optional[str] = Field(alias="details",default=None,)
	status: Optional[str | MultiTenantOrganizationMemberProcessingStatus] = Field(alias="status",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState
from .multi_tenant_organization_member_processing_status import MultiTenantOrganizationMemberProcessingStatus

