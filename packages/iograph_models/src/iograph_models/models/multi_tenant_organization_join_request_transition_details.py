from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MultiTenantOrganizationJoinRequestTransitionDetails(BaseModel):
	desiredMemberState: Optional[MultiTenantOrganizationMemberState] = Field(default=None,alias="desiredMemberState",)
	details: Optional[str] = Field(default=None,alias="details",)
	status: Optional[MultiTenantOrganizationMemberProcessingStatus] = Field(default=None,alias="status",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState
from .multi_tenant_organization_member_processing_status import MultiTenantOrganizationMemberProcessingStatus

